"""Render all scenes using the active environment: python render_all.py --stills."""
import argparse
from pathlib import Path
import subprocess
import sys

SCENES = [
    ("scene_01_gancho.py", "Escena01Gancho"),
    ("scene_02_memoria.py", "Escena02Memoria"),
    ("scene_03_modular.py", "Escena03Modular"),
    ("scene_04_naive.py", "Escena04Naive"),
    ("scene_05_intuicion.py", "Escena05Intuicion"),
    ("scene_06_exponentes.py", "Escena06Exponentes"),
    ("scene_07_binario.py", "Escena07Binario"),
    ("scene_08_traza.py", "Escena08Traza"),
    ("scene_09_codigo.py", "Escena09Codigo"),
    ("scene_10_cierre.py", "Escena10Cierre"),
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stills", action="store_true", help="Save final PNGs instead of videos")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    logs = root / "media" / "verification"
    logs.mkdir(parents=True, exist_ok=True)
    failures = []
    for filename, scene in SCENES:
        # command = [sys.executable, "-m", "manim", "-ql", "--progress_bar", "none"]
        command = [sys.executable, "-m", "manim", "-qh", "--progress_bar", "none"]
        if args.stills:
            command.append("-s")
        result = subprocess.run(command + [filename, scene], cwd=root, capture_output=True, text=True)
        output = result.stdout + result.stderr
        kind = "still" if args.stills else "video"
        (logs / f"{scene}_{kind}.log").write_text(output)
        issues = result.returncode != 0 or "WARNING" in output or "Warning:" in output
        print(f"{'FAIL' if issues else 'PASS'} {scene} ({kind})", flush=True)
        if issues:
            print(output, flush=True)
            failures.append(scene)
    if failures:
        raise SystemExit(f"Review failed scenes: {', '.join(failures)}")


if __name__ == "__main__":
    main()
