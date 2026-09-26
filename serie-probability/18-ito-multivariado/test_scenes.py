"""Contratos del guion y comprobaciones numéricas sin renderizar."""
import ast
from pathlib import Path
import re
import unittest
import numpy as np
from scene_utils import correlation_points

ROOT = Path(__file__).resolve().parent


class SceneContracts(unittest.TestCase):
    def test_eight_modules_and_triggers(self):
        scenes = sorted(ROOT.glob('scene_[0-9][0-9]_*.py'))
        script = (ROOT / 'guion.md').read_text()
        self.assertEqual(len(scenes), 8)
        self.assertEqual(len(re.findall(r'^#### Escena:', script, re.M)), 8)
        for index, file in enumerate(scenes, 1):
            source = file.read_text()
            self.assertTrue(file.name.startswith(f'scene_{index:02}_'))
            self.assertEqual(re.findall(r'\[TRIGGER_(\d+)\]', source), ['1', '2', '3'])
            tree = ast.parse(source)
            classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
            self.assertEqual(len(classes), 1)
            self.assertTrue(classes[0].name.startswith(f'Escena{index:02}'))
            construct = next(n for n in classes[0].body if isinstance(n, ast.FunctionDef) and n.name == 'construct')
            self.assertEqual(ast.unparse(construct.body[0]), 'self.camera.background_color = BG_COLOR')
            self.assertTrue(any(isinstance(n, ast.ImportFrom) and n.module == 'styles.theme' for n in tree.body))

    def test_only_latex_and_central_palette(self):
        for file in list(ROOT.glob('scene_*.py')):
            source = file.read_text()
            self.assertIsNone(re.search(r'#[0-9A-Fa-f]{6}\b', source))
            for node in ast.walk(ast.parse(source)):
                if isinstance(node, ast.Call):
                    name = getattr(node.func, 'id', getattr(node.func, 'attr', ''))
                    self.assertNotIn(name, {'Text', 'MarkupText', 'Paragraph', 'DecimalNumber', 'Integer'})

    def test_correlated_samples_and_degenerate_limits(self):
        base = np.random.default_rng(1801).standard_normal((3000, 2))
        for rho in [0, .7, -.7, 1, -1]:
            points = correlation_points(base, rho)
            np.testing.assert_allclose(np.cov(points, rowvar=False), [[1, rho], [rho, 1]], atol=.07)
        np.testing.assert_array_equal(correlation_points(base, 1)[:, 1], base[:, 0])
        np.testing.assert_array_equal(correlation_points(base, -1)[:, 1], -base[:, 0])
        with self.assertRaises(ValueError):
            correlation_points(base, 1.1)

    def test_nested_mesh_preserves_terminal_values(self):
        fine = np.random.default_rng(1803).standard_normal((4096, 2))/np.sqrt(4096)
        for rho in [0, .7, 1]:
            dw = correlation_points(fine, rho)
            for n in [16, 64, 256]:
                coarse = dw.reshape(n, 4096//n, 2).sum(axis=1)
                np.testing.assert_allclose(coarse.sum(axis=0), dw.sum(axis=0), atol=1e-13)

    def test_ito_contractions_and_double_correlation(self):
        rho = .6
        R = np.array([[1., rho], [rho, 1.]])
        hessian_product = np.array([[0., 1.], [1., 0.]])
        self.assertAlmostEqual(.5*np.trace(R@hessian_product), rho)
        G = np.array([[1., 0.], [0., 1.], [1., 1.]])
        self.assertAlmostEqual(.5*np.trace((G@G.T)@(2*np.eye(3))), np.sum(G*G))
        L = np.array([[1., 0.], [.6, .8]])
        np.testing.assert_allclose((G@L)@(G@L).T, G@R@G.T)
        self.assertAlmostEqual(((L@L)@(L@L).T)[1,1], 1.576)

    def test_ou_energy_balance(self):
        x0_squared = 1.1**2 + .6**2
        self.assertAlmostEqual(x0_squared, 1.57)
        for t in [0, .5, 1, 4]:
            e = .25 + 1.32*np.exp(-2*t)
            derivative = -2*1.32*np.exp(-2*t)
            self.assertAlmostEqual(derivative, -2*e+.5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
