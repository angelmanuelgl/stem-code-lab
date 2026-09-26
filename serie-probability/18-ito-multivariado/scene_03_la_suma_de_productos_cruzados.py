"""Escena 03: particiones anidadas de una única realización browniana."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from styles.theme import (
    BG_COLOR, TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT,
    ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN,
)
from manim import *
from scene_utils import np, heading, conclusion, math, prose, stack, axes, correlation_points, polyline


class Escena03LaSumaDeProductosCruzados(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        heading(self, "La suma de productos cruzados")
        fine = np.random.default_rng(1803).standard_normal((4096, 2))/np.sqrt(4096)
        def products(n, rho):
            dw = correlation_points(fine, rho).reshape(n, 4096//n, 2).sum(axis=1)
            return dw[:, 0]*dw[:, 1]
        bound = max(np.max(np.abs(products(16, r))) for r in [.7, 0, 1])*1.15
        ax = axes([0, 1, .25], [-bound, bound, bound], 5.2, 2.5, LEFT*3.15+UP*.65)
        def bars(n, rho):
            result = VGroup()
            for k, value in enumerate(products(n, rho)):
                start, end = ax.c2p((k+.5)/n, 0), ax.c2p((k+.5)/n, value)
                rect = Rectangle(width=5.2/n*.8, height=max(abs(end[1]-start[1]), .005),
                                 fill_color=ACCENT_MINT if value >= 0 else ACCENT_VINO,
                                 fill_opacity=.85, stroke_width=0).move_to((start+end)/2)
                result.add(rect)
            return result
        def counter(n, rho):
            return math(rf"N={n},\quad S_N={products(n,rho).sum():.3f}", 32,
                        ACCENT_TERRACOTTA).move_to(LEFT*3.15+DOWN*.85)
        histogram, count = bars(16, .7), counter(16, .7)
        title = math(r"\Delta W_{1,k}\,\Delta W_{2,k}\quad(T=1)", 28).next_to(ax, UP)
        summation = math(r"S_N=\sum_{k=0}^{N-1}\Delta W_{1,k}\Delta W_{2,k}", 33)
        summation.move_to(RIGHT*3.1+UP*1.8)
        # [TRIGGER_1] Productos con signo; el contador usa exactamente las barras.
        self.play(Create(ax), Write(title), Create(histogram), Write(count), Write(summation), run_time=3)
        sum_ax = axes([0, 1, .25], [-.2, 1.4, .4], 5.2, 1.2, LEFT*3.15+DOWN*1.7)
        def cumulative(n, rho):
            return polyline(sum_ax, np.linspace(0, 1, n+1),
                            np.r_[0, products(n, rho).cumsum()], ACCENT_CYAN)
        def reference(rho):
            return DashedLine(sum_ax.c2p(0, rho), sum_ax.c2p(1, rho),
                              color=ACCENT_MINT, stroke_width=2)
        accumulated, target_line = cumulative(16, .7), reference(.7)
        target = math(r"\rho=0.7,\quad \rho T=0.700", 28, ACCENT_MINT).move_to(LEFT*3.15+DOWN*2.6)
        self.play(Create(sum_ax), Create(accumulated), Create(target_line), Write(target))
        self.wait(4)
        limit = stack(math(r"S_N\xrightarrow{L^2}\rho T", 38, ACCENT_MINT),
                      math(r"\mathbb E S_N=\rho T", 32),
                      math(r"\operatorname{Var}(S_N)=(1+\rho^2)T^2/N", 30),
                      math(r"\operatorname{Var}(S_\pi)\le(1+\rho^2)T|\pi|", 30),
                      center=RIGHT*3.1+DOWN*.2, buff=.5)
        # [TRIGGER_2] Agrupar incrementos finos, nunca volver a sortearlos.
        for n in [64, 256]:
            self.play(ReplacementTransform(histogram, new_bars := bars(n, .7)),
                      Transform(count, counter(n, .7)),
                      Transform(accumulated, cumulative(n, .7)), run_time=2)
            histogram = new_bars
            self.wait(2)
        self.play(Write(limit), run_time=3)
        self.wait(4)
        # [TRIGGER_3] Fuentes independientes frente a variación de una misma fuente.
        for rho in [0, 1]:
            self.play(Transform(histogram, bars(256, rho)), Transform(count, counter(256, rho)),
                      Transform(accumulated, cumulative(256, rho)),
                      Transform(target_line, reference(rho)),
                      Transform(target, math(rf"\rho={rho},\quad \rho T={rho:.3f}", 28,
                                            ACCENT_MINT).move_to(target)), run_time=2)
            self.wait(3)
        self.play(Write(math(r"dW_i\,dW_j=R_{ij}\,dt", 34, ACCENT_CYAN)
                        .move_to(RIGHT*3.1+DOWN*2.4)))
        conclusion(self, "Una suma finita fluctúa; el límite en media cuadrática no.")
