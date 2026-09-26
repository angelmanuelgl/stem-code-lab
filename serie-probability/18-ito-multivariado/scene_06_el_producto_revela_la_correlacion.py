"""Escena 06: producto de Wiener, dos derivadas mixtas y media simulada."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from styles.theme import (
    BG_COLOR, TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT,
    ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN,
)
from manim import *
from scene_utils import np, heading, conclusion, math, prose, stack, axes, polyline


class Escena06ElProductoRevelaLaCorrelacion(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        heading(self, "El producto revela la correlación")
        derivatives = stack(math(r"f(x,y)=xy", 40),
                            math(r"\nabla f=\begin{pmatrix}y\\x\end{pmatrix}", 36),
                            math(r"D^2f=\begin{pmatrix}0&1\\1&0\end{pmatrix}", 36),
                            math(r"f_{xx}=f_{yy}=0,\quad f_{xy}=f_{yx}=1", 30),
                            center=LEFT*3.15+UP*.1, buff=.4)
        covariance = math(r"a=R=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}", 36)
        covariance.move_to(RIGHT*3.15+UP*1.8)
        # [TRIGGER_1] Derivadas completas, incluidas ambas entradas mixtas.
        for row in derivatives:
            self.play(Write(row), run_time=.9)
        self.play(Write(covariance)); self.wait(3)
        mixed = stack(math(r"\frac12\sum_{i,j}a_{ij}f_{ij}", 36),
                      math(r"=\frac12(0+\rho\cdot1+\rho\cdot1+0)", 33),
                      math(r"=\frac12(2\rho)=\rho", 38, ACCENT_MINT),
                      center=RIGHT*3.15+DOWN*.3, buff=.5)
        # [TRIGGER_2] Mostrar y contar las contribuciones (1,2) y (2,1).
        for row in mixed:
            self.play(Write(row))
        self.play(Circumscribe(mixed[1], color=ACCENT_TERRACOTTA))
        self.wait(3)
        product_rule = stack(math(r"d(W_1W_2)=", 36),
                             math(r"W_2\,dW_1+W_1\,dW_2+\rho\,dt", 34),
                             math(r"\mathbb E\!\int_0^t W_2\,dW_1", 30),
                             math(r"=\mathbb E\!\int_0^t W_1\,dW_2=0", 30),
                             math(r"\mathbb E[W_1(t)W_2(t)]=\rho t", 34, ACCENT_MINT),
                             center=RIGHT*3.15, buff=.42)
        self.play(FadeOut(covariance), FadeOut(mixed), FadeOut(derivatives), run_time=1)
        # [TRIGGER_3] Promedio real de 4000 trayectorias: no sustituirlo por rho*t.
        rng = np.random.default_rng(1806)
        m, n, rho = 4000, 128, .7
        z = rng.standard_normal((m, n, 2))/np.sqrt(n)
        w1 = np.cumsum(z[:, :, 0], axis=1)
        w2 = rho*w1+np.sqrt(1-rho*rho)*np.cumsum(z[:, :, 1], axis=1)
        samples = w1*w2
        mean = np.r_[0, samples.mean(axis=0)]
        se = np.r_[0, samples.std(axis=0, ddof=1)/np.sqrt(m)]
        t = np.linspace(0, 1, n+1)
        ax = axes([0, 1, .25], [-.1, 1, .25], 5.2, 3.4, LEFT*3.15+UP*.15)
        theoretical = polyline(ax, t, rho*t, ACCENT_MINT, 3)
        empirical = polyline(ax, t, mean, ACCENT_CYAN, 2)
        band = Polygon(*[ax.c2p(x, y) for x,y in zip(t, mean+2*se)],
                       *[ax.c2p(x, y) for x,y in zip(t[::-1], (mean-2*se)[::-1])],
                       fill_color=ACCENT_CYAN, fill_opacity=.15, stroke_width=0)
        axis_labels = VGroup(math("t", 26).next_to(ax, RIGHT),
                             math(r"\overline{W_1W_2}", 26).next_to(ax, UP))
        legend = stack(math(r"\rho=0.7,\quad M=4000", 28),
                       prose(r"Media muestral y banda puntual $\pm2$ SE", 25, ACCENT_CYAN),
                       math(r"\rho t\quad\text{(valor exacto)}", 28, ACCENT_MINT),
                       center=LEFT*3.15+DOWN*2.15, buff=.2)
        self.play(Create(ax), Write(axis_labels), FadeIn(band), Create(theoretical),
                  Create(empirical), Write(legend), run_time=3)
        for row in product_rule:
            self.play(Write(row))
        self.wait(4)
        conclusion(self, "La corrección de Itô recupera la covarianza conocida.")
