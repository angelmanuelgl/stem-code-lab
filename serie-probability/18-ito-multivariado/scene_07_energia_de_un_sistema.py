"""Escena 07: OU exacto en la malla y balance de energía media."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from styles.theme import (
    BG_COLOR, TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT,
    ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN,
)
from manim import *
from scene_utils import np, heading, conclusion, math, prose, stack, axes, polyline


class Escena07EnergiaDeUnSistema(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        heading(self, "Energía de un sistema")
        theta, sigma, n, h = 1., .5, 2, 1/128
        x0 = np.array([1.1, .6])
        samples = [x0]
        rng = np.random.default_rng(1807)
        decay = np.exp(-theta*h)
        noise_sd = sigma*np.sqrt((1-decay*decay)/(2*theta))
        for _ in range(512):
            samples.append(decay*samples[-1]+noise_sd*rng.standard_normal(n))
        samples = np.array(samples)
        ax = axes([-2, 2, 1], [-2, 2, 1], 3.15, 3.15, LEFT*3.15+UP*.65)
        path = polyline(ax, samples[:, 0], samples[:, 1], ACCENT_CYAN, 1.4)
        particle = Dot(ax.c2p(*x0), color=ACCENT_TERRACOTTA, radius=.065)
        ring = always_redraw(lambda: Circle(radius=max(np.linalg.norm(particle.get_center()-ax.c2p(0,0)), .001),
                                           color=ACCENT_INDIGO, stroke_width=1.5).move_to(ax.c2p(0,0)))
        pull = Arrow(ax.c2p(*x0), ax.c2p(0,0), buff=.1, color=ACCENT_MINT)
        derivatives = stack(math(r"f(X)=\|X\|^2", 38), math(r"\nabla f=2X,\quad D^2f=2I_n", 34),
                            math(r"b=-\theta X,\quad G=\sigma I_n", 34),
                            center=RIGHT*3.15+UP*1.1)
        # [TRIGGER_1] Radio ||X|| y atracción hacia el origen; transición OU exacta.
        self.play(Create(ax), FadeIn(particle), Create(ring), Create(pull), Write(derivatives), run_time=3)
        self.wait(3)
        self.play(FadeOut(pull), Create(path), MoveAlongPath(particle, path), run_time=8, rate_func=linear)
        trace = stack(math(r"\frac12\operatorname{tr}(GG^\top 2I_n)", 34),
                      math(r"=\operatorname{tr}(GG^\top)=\|G\|_F^2", 34, ACCENT_MINT),
                      math(r"d\|X\|^2=(2X^\top b+\|G\|_F^2)dt", 32),
                      math(r"\qquad{}+2X^\top G\,dB", 34, ACCENT_CYAN),
                      center=RIGHT*3.15, buff=.5)
        # [TRIGGER_2] El factor dos de la Hessiana cancela el medio.
        self.play(ReplacementTransform(derivatives, trace), run_time=2)
        self.play(Circumscribe(trace[1], color=ACCENT_MINT)); self.wait(4)
        balance = stack(math(r"\theta=1,\quad\sigma=0.5,\quad n=2", 32),
                        math(r"e(t)=\mathbb E\|X_t\|^2", 34),
                        math(r"e'(t)=-2e(t)+0.5", 36, ACCENT_MINT),
                        math(r"e(0)=1.57", 32),
                        math(r"e(t)=0.25+1.32e^{-2t}", 34),
                        math(r"e(\infty)=0.25", 34, ACCENT_MINT),
                        center=RIGHT*3.15, buff=.35)
        # [TRIGGER_3] Barras de deriva e inyección para la MEDIA, no para una senda.
        self.play(ReplacementTransform(trace, balance), run_time=2)
        clock = ValueTracker(0)
        def mean_energy():
            return .25+1.32*np.exp(-2*clock.get_value())
        baseline = LEFT*3.15+DOWN*1.8
        def loss_bar():
            height = 2*mean_energy()*.3
            return Rectangle(width=.65, height=height, stroke_width=0, fill_color=ACCENT_VINO,
                             fill_opacity=.8).move_to(baseline+LEFT*.85+DOWN*height/2)
        def gain_bar():
            return Rectangle(width=.65, height=.15, stroke_width=0, fill_color=ACCENT_MINT,
                             fill_opacity=.8).move_to(baseline+RIGHT*.85+UP*.075)
        loss, gain = always_redraw(loss_bar), gain_bar()
        labels = VGroup(math(r"-2e(t)", 27, ACCENT_VINO).move_to(LEFT*4+DOWN*1.45),
                        math(r"+0.5", 27, ACCENT_MINT).move_to(LEFT*2.3+DOWN*1.35),
                        prose("Balance de energía media", 25).move_to(LEFT*3.15+DOWN*1.05))
        line = Line(baseline+LEFT*1.7, baseline+RIGHT*1.7, color=TEXT_MUTED)
        self.play(Create(line), FadeIn(loss), FadeIn(gain), Write(labels))
        self.play(clock.animate.set_value(4), run_time=6, rate_func=linear)
        loss.clear_updaters(); ring.clear_updaters()
        conclusion(self, "La deriva disipa energía media; el ruido la repone.")
