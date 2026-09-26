"""Verificación reproducible: python render_all.py [--videos]."""
import argparse
import ast
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--videos', action='store_true', help='Renderizar MP4 además de validar ejecución.')
    args = parser.parse_args()
    logs = ROOT / 'media' / 'verification'
    logs.mkdir(parents=True, exist_ok=True)
    scripts = sorted(ROOT.glob('scene_[0-9][0-9]_*.py'))
    assert len(scripts) == 8, 'Deben existir ocho módulos de escena.'
    results = []
    for script in scripts:
        tree = ast.parse(script.read_text())
        classes = [n.name for n in tree.body if isinstance(n, ast.ClassDef)]
        assert len(classes) == 1
        forbidden = {'Text', 'MarkupText', 'Paragraph'}
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = getattr(node.func, 'id', getattr(node.func, 'attr', ''))
                assert name not in forbidden, (script.name, name)
        command = [sys.executable, '-m', 'manim', '-ql']
        if not args.videos:
            command.append('-s')
        command += ['--disable_caching', script.name, classes[0]]
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
        start = time.monotonic()
        result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True)
        mode = 'video' if args.videos else 'still'
        log = logs / f'{script.stem}_{mode}.log'
        log.write_text(result.stdout+'\n'+result.stderr)
        results.append(dict(file=script.name, scene=classes[0], command=command,
                            returncode=result.returncode, seconds=round(time.monotonic()-start, 2),
                            log=str(log.relative_to(ROOT))))
        print(f'{script.name}: salida {result.returncode}', flush=True)
        if result.returncode:
            print((result.stdout+'\n'+result.stderr)[-6000:], flush=True)
    (logs / f'results_{mode}.json').write_text(json.dumps(results, indent=2))
    return int(any(item['returncode'] for item in results))


if __name__ == '__main__':
    raise SystemExit(main())
