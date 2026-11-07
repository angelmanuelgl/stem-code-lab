#!/usr/bin/env python3
import argparse
import shutil
import sys
import argparse
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

def open_folder(path: Path) -> None:
    """Abre la carpeta de destino en el explorador de archivos del SO."""
    try:
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", str(path)])
        else:  # Linux
            subprocess.run(["xdg-open", str(path)])
    except Exception as e:
        print(f"No se pudo abrir la carpeta automáticamente: {e}")


def resolve_target_dir(target_input: str) -> Path:
    """Resuelve rutas absolutas, relativas o con prefijos cortos dentro del sistema de archivos.

    Complejidad Temporal: O(N) donde N es el número de elementos en el directorio padre.
    """
    input_path = Path(target_input)

    # 1. Si la ruta ingresada existe directamente como directorio, usarla
    if input_path.is_dir():
        return input_path.resolve()

    # 2. Búsqueda por prefijo dentro del directorio padre especificado
    parent = input_path.parent if input_path.parent != Path(".") else Path(".")
    prefix = input_path.name

    if parent.exists() and parent.is_dir():
        matches = [
            d
            for d in parent.iterdir()
            if d.is_dir()
            and (d.name.startswith(prefix) or d.name.startswith(f"{prefix}-"))
        ]

        if len(matches) == 1:
            return matches[0].resolve()
        elif len(matches) > 1:
            print(
                f"Error: El prefijo '{prefix}' es ambiguo en '{parent}'. Coincidencias:"
            )
            for m in matches:
                print(f"  - {m.name}")
            sys.exit(1)

    print(
        f"Error: No se encontró ninguna carpeta que coincida con '{target_input}'."
    )
    sys.exit(1)


def get_unique_destination(dest_dir: Path, filename: str) -> Path:
    """Resuelve colisiones de nombres generando sufijos numéricos únicos.

    Complejidad Temporal: O(C) donde C es el número de colisiones existentes.
    """
    target = dest_dir / filename
    if not target.exists():
        return target

    stem = target.stem
    suffix = target.suffix
    counter = 1
    while True:
        candidate = dest_dir / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def collect_manim_videos(target_input: str, quality: str) -> None:
    root_dir = resolve_target_dir(target_input)
    dest_dir = root_dir / "resultados" / quality

    print(f"Directorio Raíz Resuelto: {root_dir}")
    print(f"Calidad a extraer:        {quality}")
    print(f"Carpeta Destino:          {dest_dir}\n")

    # Conjunto de nombres de carpetas reservadas/excluidas
    excluded_dirs = {"partial_movie_files", "resultados"}

    # 1. Localizar todos los directorios 'media' dentro de la estructura
    media_directories = [
        d
        for d in root_dir.rglob("media")
        if d.is_dir() and not any(part in excluded_dirs for part in d.parts)
    ]

    if not media_directories:
        print(
            f"Error: No se encontró ninguna carpeta 'media' dentro de: {root_dir}"
        )
        sys.exit(1)

    # Si la carpeta de resultados ya existe, eliminar su contenido previo
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    copied_count = 0

    # 2. Recorrer cada directorio 'media' encontrado
    for media_dir in media_directories:
        for quality_dir in media_dir.rglob(quality):
            if not quality_dir.is_dir():
                continue

            # Invariante de exclusión: descartar renderizados parciales y la carpeta de salida
            if any(part in excluded_dirs for part in quality_dir.parts):
                continue

            for video_file in quality_dir.glob("*.mp4"):
                if video_file.is_file():
                    target_path = get_unique_destination(
                        dest_dir, video_file.name
                    )
                    shutil.copy2(video_file, target_path)
                    print(
                        f"  [+] Copiado: {video_file.relative_to(root_dir)} -> {target_path.name}"
                    )
                    copied_count += 1

    print(
        f"\nProceso finalizado. Total de videos recolectados: {copied_count}"
    )
    print(f"Ubicación final: {dest_dir}")

    open_folder(dest_dir)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Recolecta renders de Manim buscando recursivamente carpetas 'media'."
    )
    parser.add_argument(
        "target_path",
        type=str,
        help="Ruta o prefijo del directorio raíz (ej. 'serie-icpc-problems/HardcoreHangman')",
    )
    parser.add_argument(
        "quality",
        type=str,
        help="Nombre de la carpeta de calidad (ej. '480p15', '1080p60')",
    )

    args = parser.parse_args()
    collect_manim_videos(args.target_path, args.quality)