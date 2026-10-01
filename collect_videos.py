# # Usando prefijo corto
# python3 collect_videos.py serie-probability/04 480p15

# # Usando el nombre completo del directorio
# python3 collect_videos.py serie-probability/04-convergencia-casi-segura-y-en-probabilidad 1080p60

# # Funciona también con otras subcarpetas del repositorio
# python3 collect_videos.py computerscience-standalone/01 1080p60



#!/usr/bin/env python3
import argparse
import shutil
import sys
from pathlib import Path


def resolve_target_dir(target_input: str) -> Path:
    """Resuelve rutas absolutas, relativas o con prefijos cortos.

    Ejemplos soportados:
      - 'serie-probability/04'  -> 'serie-probability/04-convergencia-casi-segura...'
      - 'serie-probability/04-convergencia-casi-segura-y-en-probabilidad'
      - '04' (si se ejecuta estando dentro de serie-probability/)
    """
    input_path = Path(target_input)

    # 1. Si la ruta ingresada existe directamente como directorio, usarla
    if input_path.is_dir():
        return input_path.resolve()

    # 2. Búsqueda por prefijo dentro del directorio padre especificado
    parent = input_path.parent if input_path.parent != Path(".") else Path(".")
    prefix = input_path.name

    if parent.exists() and parent.is_dir():
        # Coincidir carpetas que inicien con el prefijo (ej: '04', '04-')
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


def collect_manim_videos(target_input: str, quality: str) -> None:
    video_dir = resolve_target_dir(target_input)
    media_dir = video_dir / "media"

    if not media_dir.exists():
        print(f"Error: No se encontró la carpeta 'media' en: {video_dir}")
        sys.exit(1)

    dest_dir = media_dir / f"all_{quality}"
    dest_dir.mkdir(parents=True, exist_ok=True)

    print(f"Directorio resuelto: {video_dir}")
    print(f"Calidad a extraer:   {quality}")
    print(f"Carpeta destino:     {dest_dir}\n")

    copied_count = 0

    # Recorrer subdirectorios dentro de media/ buscando carpetas con el nombre de la calidad
    for quality_dir in media_dir.rglob(quality):
        parts = quality_dir.parts

        # Invariante: Ignorar renderizados parciales y la misma carpeta de salida
        if "partial_movie_files" in parts or f"all_{quality}" in parts:
            continue

        if quality_dir.is_dir():
            for video_file in quality_dir.glob("*.mp4"):
                if video_file.is_file():
                    dest_file = dest_dir / video_file.name
                    shutil.copy2(video_file, dest_file)
                    print(f"  [+] Copiado: {video_file.name}")
                    copied_count += 1

    print(f"\nProceso finalizado. Total de videos recolectados: {copied_count}")
    print(f"Ubicación: {dest_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Recolecta renders de Manim resolviendo prefijos de carpetas."
    )
    parser.add_argument(
        "target_path",
        type=str,
        help="Ruta o prefijo (ej. 'serie-probability/04' o 'serie-probability/02-integral-de-lebesgue')",
    )
    parser.add_argument(
        "quality",
        type=str,
        help="Nombre de la carpeta de calidad (ej. '480p15', '1080p60')",
    )

    args = parser.parse_args()
    collect_manim_videos(args.target_path, args.quality)