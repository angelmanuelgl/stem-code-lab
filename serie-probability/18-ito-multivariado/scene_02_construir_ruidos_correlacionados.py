"""Escena 02: mezcla lineal y pérdida de rango en rho=+-1."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from styles.theme import (
    BG_COLOR, TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT,
    ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN,
)
from manim import *
from scene_utils import (np, heading, conclusion, math, prose, stack, axes,
                         covariance_ellipse, box, arrow_between)


class Escena02ConstruirRuidosCorrelacionados(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        heading(self, "Construir ruidos correlacionados")
        b1 = box("B_1", LEFT*5.3+UP*1.8)
        b2 = box("B_2", LEFT*5.3+UP*.2)
        mix = box(r"\sum", LEFT*2.8+UP*1, 1, 1.2)
        output = box("W_2", LEFT*.6+UP*1, 1)
        edges = VGroup(Arrow(b1.get_right(), mix.get_left()+UP*.3, color=ACCENT_CYAN),
                       Arrow(b2.get_right(), mix.get_left()+DOWN*.3, color=ACCENT_CYAN),
                       arrow_between(mix, output))
        weights = VGroup(math(r"\rho", 28, ACCENT_TERRACOTTA).move_to(LEFT*4+UP*2),
                         math(r"\sqrt{1-\rho^2}", 28, ACCENT_TERRACOTTA).move_to(LEFT*3.9+DOWN*.05))
        recipe = stack(math(r"W_1=B_1"), math(r"W_2=\rho B_1+\sqrt{1-\rho^2}B_2", 32),
                       math(r"B_1\perp\!\!\!\perp B_2", 30), center=RIGHT*3.15+UP*1.3)
        # [TRIGGER_1] Construcción a partir de fuentes independientes.
        self.play(FadeIn(b1), FadeIn(b2), FadeIn(mix), FadeIn(output), Create(edges),
                  Write(weights), Write(recipe), run_time=3)
        self.wait(5)
        moments = stack(math(r"\operatorname{Var}(W_2(t))", 32),
                        math(r"=\rho^2t+(1-\rho^2)t=t", 32),
                        math(r"\operatorname{Cov}(W_1(t),W_2(t))=\rho t", 30),
                        math(r"R=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\succeq0", 34),
                        math(r"\lambda(R)=1\pm\rho\ge0\iff |\rho|\le1", 30),
                        center=RIGHT*3.15, buff=.35)
        # [TRIGGER_2] Cálculo explícito de varianzas y restricción PSD.
        self.play(FadeOut(recipe), run_time=.6)
        for row in moments:
            self.play(Write(row), run_time=1)
        ax = axes([-2.5, 2.5, 1], [-2.5, 2.5, 1], 2.1, 2.1, LEFT*3.1+DOWN*1.55)
        ellipse = covariance_ellipse(ax, .7)
        note = math(r"\rho=0.7", 27, ACCENT_TERRACOTTA).next_to(ax, RIGHT, buff=.25)
        self.play(Create(ax), Create(ellipse), Write(note))
        self.wait(4)
        # [TRIGGER_3] La elipse degenerada es una recta, sin Cholesky singular.
        for rho in [1, -1]:
            message = rf"\rho={rho},\quad W_2={'B_1' if rho == 1 else '-B_1'}"
            self.play(Transform(ellipse, covariance_ellipse(ax, rho)),
                      Transform(note, math(message, 26, ACCENT_TERRACOTTA, width=2.8)
                                .next_to(ax, RIGHT, buff=.2)),
                      b2.animate.set_opacity(.25), edges[1].animate.set_opacity(.25),
                      run_time=2)
            self.wait(3)
        conclusion(self, "En los extremos queda una sola fuente efectiva: rango uno.")
