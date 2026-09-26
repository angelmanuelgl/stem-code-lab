"""Escena 04: formas matriciales y covarianza efectiva de dimensión n."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from styles.theme import (
    BG_COLOR, TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT,
    ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN,
)
from manim import *
from scene_utils import heading, conclusion, math, prose, stack, box, arrow_between


class Escena04ElEstadoYLasFuentesTienenTamanosDistintos(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        heading(self, "El estado y las fuentes tienen tamaños distintos")
        independent_label = prose("Fuentes independientes", 27).move_to(LEFT*3.15+UP*2.4)
        self.play(Write(independent_label))
        matrix = box(r"G", LEFT*4.9+UP*1, 1.6, 2.2)
        source = box(r"dB", LEFT*2.85+UP*1, .95, 1.5)
        result = box(r"G\,dB", LEFT*.8+UP*1, 1.35, 2.2, ACCENT_MINT)
        signs = VGroup(math(r"\times", 30).move_to(LEFT*3.85+UP*1),
                       math(r"=", 30).move_to(LEFT*1.85+UP*1))
        dims = VGroup(math(r"n\times m", 28).next_to(matrix, DOWN),
                      math(r"m\times1", 28).next_to(source, DOWN),
                      math(r"n\times1", 28).next_to(result, DOWN))
        equation = stack(math(r"dX=b\,dt+G\,dB", 36),
                         math(r"X\in\mathbb R^n,\ B\in\mathbb R^m", 32),
                         math(r"G\in\mathbb R^{n\times m}", 34, ACCENT_INDIGO),
                         center=RIGHT*3.15+UP*1.25)
        # [TRIGGER_1] La difusión es rectangular: aquí n=3, m=2.
        self.play(Create(matrix), Create(source), Create(result), Write(signs), Write(dims),
                  Write(equation), run_time=3)
        example = math(r"G=\begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix},\quad n=3,\ m=2", 34)
        example.move_to(LEFT*3.15+DOWN*1.45)
        self.play(Write(example)); self.wait(4)
        calc = stack(math(r"(G\,dB)(G\,dB)^\top", 34),
                     math(r"=G\underbrace{(dB\,dB^\top)}_{I_m\,dt}G^\top", 34),
                     math(r"d[X_i,X_j]_t=(GG^\top)_{ij}\,dt", 32),
                     center=RIGHT*3.15+DOWN*.1)
        # [TRIGGER_2] Ruido al cuadrado; términos dt² y dt dB no sobreviven.
        self.play(FadeOut(equation))
        for row in calc:
            self.play(Write(row))
        self.play(Transform(example, math(r"GG^\top=\begin{pmatrix}1&0&1\\0&1&1\\1&1&2\end{pmatrix}", 34)
                            .move_to(example)), run_time=2)
        self.wait(4)
        # [TRIGGER_3] La identidad de los ruidos se reemplaza por R, no por G.
        correlated = stack(math(r"dW\,dW^\top=R\,dt", 34),
                           math(r"a=GRG^\top\in\mathbb R^{n\times n}", 34, ACCENT_MINT),
                           math(r"R\in\mathbb R^{m\times m}", 30),
                           center=RIGHT*3.15, buff=.6)
        self.play(ReplacementTransform(calc, correlated), run_time=2)
        self.play(Write(prose("Fuentes correlacionadas", 27).move_to(RIGHT*3.15+UP*2.1)))
        self.play(Indicate(matrix, color=ACCENT_INDIGO), Indicate(correlated[1], color=ACCENT_MINT))
        conclusion(self, r"Difusión $G$: $n\times m$. Covarianza instantánea $a$: $n\times n$.")
