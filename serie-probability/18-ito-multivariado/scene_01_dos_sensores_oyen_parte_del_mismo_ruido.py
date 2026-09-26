"""Escena 01 del guion: 3000 incrementos y normales base compartidas."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from styles.theme import (
    BG_COLOR, TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT,
    ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN,
)
from manim import *
from scene_utils import (np, heading, conclusion, prose, math, axes, cloud,
                         polyline, correlation_points, covariance_ellipse)


class Escena01DosSensoresOyenParteDelMismoRuido(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        heading(self, "Dos sensores oyen parte del mismo ruido")
        rng = np.random.default_rng(1801)
        base = rng.standard_normal((3000, 2))
        ax = axes([-4, 4, 2], [-4, 4, 2], 4.2, 4.2, LEFT*3.4)
        labels = VGroup(math(r"\Delta W_1/\sqrt{\Delta t}", 26).next_to(ax, DOWN),
                        math(r"\Delta W_2/\sqrt{\Delta t}", 26).next_to(ax, UP, buff=.13))
        points = cloud(ax, base)
        outline = covariance_ellipse(ax, 0)
        tx = axes([0, 1, .5], [-2.8, 2.8, 1], 5.3, 1.8, RIGHT*3.15+UP*.7)
        increments = base[:128] / np.sqrt(128)
        times = np.linspace(0, 1, 129)
        def traces(rho):
            paths = np.vstack((np.zeros(2), np.cumsum(correlation_points(increments, rho), axis=0)))
            return VGroup(polyline(tx, times, paths[:, 0], ACCENT_CYAN),
                          polyline(tx, times, paths[:, 1], ACCENT_TERRACOTTA))
        paths = traces(0)
        legend = VGroup(math(r"W_1", 28, ACCENT_CYAN),
                        math(r"W_2", 28, ACCENT_TERRACOTTA)).arrange(RIGHT, buff=.65)
        legend.move_to(RIGHT*3.15+UP*2)
        slider = NumberLine(x_range=[-1, 1, .5], length=4.4, include_numbers=False,
                            color=TEXT_MUTED).move_to(RIGHT*3.15+DOWN*1)
        slider_labels = VGroup(*[math(str(v), 24).next_to(slider.n2p(v), DOWN, buff=.15)
                                 for v in [-1, 0, 1]])
        pointer = Dot(slider.n2p(0), color=ACCENT_TERRACOTTA)
        rho_label = math(r"\rho=0", 32, ACCENT_TERRACOTTA).move_to(RIGHT*3.15+DOWN*1.9)
        # [TRIGGER_1] Dos sensores y nube circular (misma escala en ambos ejes).
        self.play(Create(ax), Write(labels), FadeIn(points), Create(outline),
                  Create(tx), Create(paths), Write(legend), run_time=3)
        self.play(Create(slider), Write(slider_labels), FadeIn(pointer), Write(rho_label))
        self.wait(4)
        # [TRIGGER_2] Se reutilizan las 3000 normales: solo cambia la mezcla.
        for rho in [.7, -.7]:
            target = cloud(ax, correlation_points(base, rho))
            self.play(Transform(points, target), Transform(paths, traces(rho)),
                      Transform(outline, covariance_ellipse(ax, rho)),
                      pointer.animate.move_to(slider.n2p(rho)),
                      Transform(rho_label, math(rf"\rho={rho}", 32, ACCENT_TERRACOTTA)
                                .move_to(rho_label)), run_time=3)
            self.wait(3)
        # [TRIGGER_3] La inclinación registra el signo de la covarianza.
        formula = math(r"\operatorname{Cov}(\Delta W_1,\Delta W_2)=\rho\,\Delta t", 32)
        formula.move_to(RIGHT*3.15+DOWN*2.55)
        self.play(Write(formula), Indicate(outline, color=ACCENT_MINT), run_time=2)
        conclusion(self, "La corrección debe recordar cómo fluctúan juntos.")
