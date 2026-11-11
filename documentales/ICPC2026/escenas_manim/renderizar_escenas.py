"""Renderiza escenas registradas usando las banderas habituales de Manim.

Ejemplos:
    python renderizar_escenas.py -qh
    python renderizar_escenas.py -qk
    python renderizar_escenas.py -qh sc00
"""
import argparse
import subprocess
import sys
from pathlib import Path


# Cada entrada contiene el archivo y las clases de escena disponibles.
ESCENAS = [
    # ["sc00_gancho.py", ["Gancho"]],
    ["sc01_proceso.py", ["Proceso"]],
]


def main():
    parser = argparse.ArgumentParser(description="Renderizar escenas Manim del proyecto.")
    parser.add_argument("flags", nargs="*", help="Banderas de Manim, por ejemplo -qh, -qk o --format=mp4")
    parser.add_argument("--list", action="store_true", help="Mostrar escenas registradas")
    args, unknown = parser.parse_known_args()
    flags = args.flags + unknown
    root = Path(__file__).resolve().parent

    if args.list:
        for file, classes in ESCENAS:
            print(f"{file}: {', '.join(classes)}")
        return

    selectors = [arg.lower() for arg in flags if not arg.startswith("-")]
    manim_flags = [arg for arg in flags if arg.startswith("-")]
    quality_flags = [flag for flag in manim_flags if flag in ("-qh", "-qk", "-ql")]
    if len(quality_flags) > 1:
        parser.error("Indica solo una calidad: -qh, -qk o -ql.")
    quality_suffix = f"_{quality_flags[0][1:]}" if quality_flags else ""
    selected = [entry for entry in ESCENAS if not selectors or any(
        selector in entry[0].lower() or any(selector in cls.lower() for cls in entry[1])
        for selector in selectors
    )]
    if not selected:
        parser.error("No hay escenas que coincidan con el selector indicado.")

    for file, classes in selected:
        for scene in classes:
            output_name = f"{Path(file).stem}_{scene}{quality_suffix}"
            command = [sys.executable, "-m", "manim", *manim_flags,
                       "--output_file", output_name, str(root / file), scene]
            print("\n$ " + " ".join(command), flush=True)
            subprocess.run(command, cwd=root, check=True)


if __name__ == "__main__":
    main()
