"""Renderiza las escenas Manim CE del documental ICPC México 2026.

Ejemplos:
    python renderizar_escenas.py --list
    python renderizar_escenas.py -ql
    python renderizar_escenas.py -qh CourierOneUp
    python renderizar_escenas.py -qk sc30_final.py
    python renderizar_escenas.py --sequence -qh
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCENAS_INDEPENDIENTES = [
    # ("sc00_gancho.py", ["Gancho"]),
    # ("sc10_conceptos.py", [
    #     "EscuelaVsICPC", "PelarCebolla", "MenuTecnicas",
    #                         "DistribucionProblemas", ]),
    ("sc11_problemc.py", [
            # "EnunciadoCourier",
            "IntuicionCourier"]),
    # ("sc30_final.py", ["RolesEquipo", "TalentoReclutadores", "EntradaResultados",
    #                     "FiltroEquipos", "MedallasPorRendimiento", "TablaTop25"]),
    # ("sc40_clasificacion.py", ["AvanceLATAM", "ComparacionPuestos", "FactoresLogisticos",
    #                             "Reconocimiento", "CierreEntrevistas"]),
]
SECUENCIA_COMPLETA = ("sc01_proceso.py", ["Proceso"])


def main():
    parser = argparse.ArgumentParser(description="Renderiza escenas registradas del storyboard.")
    parser.add_argument("--list", action="store_true", help="Muestra módulos y clases disponibles")
    parser.add_argument("--sequence", action="store_true",
                        help="Renderiza un solo reel con las escenas en orden narrativo")
    parser.add_argument("--keep-going", action="store_true",
                        help="Continúa tras un fallo y reporta las escenas fallidas al final")
    parser.add_argument("items", nargs="*", help="Banderas de Manim y selectores de escena/archivo")
    args, extra = parser.parse_known_args()
    items = args.items + extra
    root = Path(__file__).resolve().parent

    if args.list:
        for filename, classes in SCENAS_INDEPENDIENTES:
            print(f"{filename}: {', '.join(classes)}")
        print("sc01_proceso.py: Proceso (reel completo; usar --sequence)")
        print(f"Escenas independientes: {sum(len(v) for _, v in SCENAS_INDEPENDIENTES)}")
        return 0

    flags = [item for item in items if item.startswith("-")]
    selectors = [item.lower() for item in items if not item.startswith("-")]
    qualities = [flag for flag in flags if flag in {"-ql", "-qm", "-qh", "-qk"}]
    if len(qualities) > 1:
        parser.error("Elige una sola calidad: -ql, -qm, -qh o -qk.")
    quality_tag = f"_{qualities[0][1:]}" if qualities else ""

    registry = [SECUENCIA_COMPLETA] if args.sequence else SCENAS_INDEPENDIENTES
    selected = []
    for filename, classes in registry:
        matching = [scene for scene in classes if not selectors or any(
            token in filename.lower() or token in scene.lower() for token in selectors
        )]
        if matching:
            selected.append((filename, matching))
    if not selected:
        parser.error("No hay coincidencias. Consulta las opciones con --list.")

    failures = []
    for filename, classes in selected:
        for scene in classes:
            outfile = f"{Path(filename).stem}_{scene}{quality_tag}"
            command = [sys.executable, "-m", "manim", *flags, "--output_file", outfile,
                       str(root / filename), scene]
            print("\n$ " + " ".join(command), flush=True)
            try:
                subprocess.run(command, cwd=root, check=True)
            except subprocess.CalledProcessError as exc:
                failures.append((filename, scene, exc.returncode))
                if not args.keep_going:
                    raise
    if failures:
        print("\nFallaron estas escenas:")
        for filename, scene, code in failures:
            print(f"  {filename} / {scene} (código {code})")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
