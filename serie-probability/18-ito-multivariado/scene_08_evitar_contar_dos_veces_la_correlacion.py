"""Escena 08: rutas equivalentes y contraejemplo a duplicar la mezcla."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from styles.theme import (
    BG_COLOR, TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT,
    ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN,
)
from manim import *
from scene_utils import np, heading, conclusion, math, prose, stack, box, arrow_between


class Escena08EvitarContarDosVecesLaCorrelacion(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        heading(self, "Evitar contar dos veces la correlación")
        def route(labels, y, color=ACCENT_INDIGO):
            xs = np.linspace(-5.8, -.65, len(labels))
            nodes = VGroup(*[box(s, np.array([x, y, 0]), .75 if len(s)<3 else .9,
                                 .7, color) for x,s in zip(xs, labels)])
            links = VGroup(*[arrow_between(a,b) for a,b in zip(nodes, nodes[1:])])
            return nodes, links
        upper, top_links = route(["dB", "L", "dW", "G", "dX"], 1.6)
        lower, low_links = route(["dB", "GL", "dX"], 0)
        names = VGroup(prose("Mezcla explícita", 26).move_to(LEFT*3.2+UP*2.3),
                       prose("Difusión compuesta", 26).move_to(LEFT*3.2+UP*.7))
        equations = stack(math(r"R=LL^\top", 36), math(r"dW=L\,dB", 36),
                          math(r"G\,dW=GL\,dB", 36),
                          center=RIGHT*3.15+UP*.85)
        # [TRIGGER_1] Dos rutas distintas desde el mismo ruido independiente.
        self.play(FadeIn(upper), Create(top_links), Write(names[0]), run_time=2)
        self.play(FadeIn(lower), Create(low_links), Write(names[1]), Write(equations), run_time=2)
        for nodes, links in [(upper, top_links), (lower, low_links)]:
            signal = Dot(nodes[0].get_center(), color=ACCENT_MINT, radius=.06)
            self.add(signal)
            for node in nodes[1:]:
                self.play(signal.animate.move_to(node.get_center()), run_time=.5)
            self.remove(signal)
        self.wait(3)
        proof = stack(math(r"a_1=G\,R\,G^\top", 36),
                      math(r"a_2=(GL)(GL)^\top", 36),
                      math(r"=G(LL^\top)G^\top=a_1", 34, ACCENT_MINT),
                      center=RIGHT*3.15+UP*.5, buff=.55)
        # [TRIGGER_2] Multiplicación de covarianzas, con idéntico resultado n×n.
        self.play(ReplacementTransform(equations, proof), run_time=2)
        self.play(Circumscribe(proof[2], color=ACCENT_MINT)); self.wait(4)
        # [TRIGGER_3] La ruta errónea contiene DOS factores L, no es equivalente.
        wrong, bad_links = route(["dB", "L", "L", "G", "dX"], -1.85, ACCENT_VINO)
        bad_name = prose("Error: mezclar otra vez", 26, ACCENT_VINO).move_to(LEFT*3.2+DOWN*1.15)
        self.play(FadeIn(wrong), Create(bad_links), Write(bad_name))
        cross = Cross(wrong[2], stroke_color=ACCENT_VINO, stroke_width=5)
        self.play(Create(cross))
        error_formula = math(r"a_{\rm error}=GLL\,L^\top L^\top G^\top", 30, ACCENT_VINO)
        error_formula.move_to(RIGHT*3.15+DOWN*1.45)
        check = math(r"G=I,\ \rho=0.6:\quad (a_{\rm error})_{22}=1.576\ne1", 28, ACCENT_VINO)
        check.move_to(RIGHT*3.15+DOWN*2.2)
        L = np.array([[1., 0.], [.6, .8]])
        assert np.allclose(L@L.T, [[1., .6], [.6, 1.]])
        assert np.isclose(((L@L)@(L@L).T)[1,1], 1.576)
        self.play(Write(error_formula), Write(check), run_time=2)
        conclusion(self, r"Control final: dimensiones correctas y la misma matriz $a$.")
