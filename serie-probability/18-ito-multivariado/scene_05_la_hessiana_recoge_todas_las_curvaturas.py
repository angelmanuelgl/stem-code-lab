"""Escena 05: superficie en proyección oblicua, Hessiana y contracción."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from styles.theme import (
    BG_COLOR, TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT,
    ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN,
)
from manim import *
from scene_utils import np, heading, conclusion, math, prose, stack


class Escena05LaHessianaRecogeTodasLasCurvaturas(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        heading(self, "La Hessiana recoge todas las curvaturas")
        origin = LEFT*3.4+UP*.25
        def project(x, y, z):
            return origin + .85*np.array([.9*x+.55*y, -.32*x+.48*y+.85*z, 0])
        def f(x, y):
            return .3*x*x+.15*x*y+.4*y*y
        surface = VGroup()
        values = np.linspace(-1.4, 1.4, 40)
        for fixed in np.linspace(-1.4, 1.4, 13):
            for swap in [False, True]:
                points = [project(v, fixed, f(v, fixed)) if not swap
                          else project(fixed, v, f(fixed, v)) for v in values]
                curve = VMobject(color=ACCENT_INDIGO, stroke_width=1.5).set_points_as_corners(points)
                surface.add(curve)
        floor = VGroup(Line(project(-1.7, 0, 0), project(1.7, 0, 0), color=TEXT_MUTED),
                       Line(project(0, -1.7, 0), project(0, 1.7, 0), color=TEXT_MUTED))
        labels = VGroup(math("x", 26).move_to(project(1.9, 0, 0)),
                        math("y", 26).move_to(project(0, 1.9, 0)))
        surface_name = math(r"f(x,y)=0.3x^2+0.15xy+0.4y^2", 28).move_to(LEFT*3.2+UP*2.25)
        gradient = Arrow(project(.5, -.3, 0), project(1.265, -.795, 0),
                         buff=0, color=ACCENT_TERRACOTTA, stroke_width=3)
        grad_label = math(r"\nabla f", 28, ACCENT_TERRACOTTA).next_to(gradient, DOWN)
        taylor = stack(math(r"f\in C^{1,2}", 32, ACCENT_MINT),
                       math(r"\Delta f\approx f_t\Delta t+\nabla f^\top\Delta X", 32),
                       math(r"\qquad+\frac12\Delta X^\top D^2f\,\Delta X", 32),
                       math(r"=\cdots+\frac12\sum_{i,j}f_{x_ix_j}\Delta X_i\Delta X_j", 30),
                       center=RIGHT*3.15+UP*.6, buff=.5)
        # [TRIGGER_1] Curvatura sobre una superficie; Taylor no descarta orden dos.
        self.play(Create(floor), Create(surface), Write(labels), Write(surface_name),
                  Create(gradient), Write(grad_label), Write(taylor), run_time=4)
        self.wait(5)
        a = Matrix([["a_{11}", "a_{12}"], ["a_{21}", "a_{22}"]],
                   element_to_mobject=lambda s: math(s, 36)).set_color(ACCENT_CYAN)
        hessian = Matrix([["f_{xx}", "f_{xy}"], ["f_{yx}", "f_{yy}"]],
                         element_to_mobject=lambda s: math(s, 36)).set_color(ACCENT_INDIGO)
        a.scale(.8).move_to(LEFT*4.6+DOWN*1.8)
        hessian.scale(.8).move_to(LEFT*1.65+DOWN*1.8)
        matrix_names = VGroup(math("a", 28, ACCENT_CYAN).next_to(a, UP, buff=.1),
                             math(r"D^2f", 28, ACCENT_INDIGO).next_to(hessian, UP, buff=.1))
        # [TRIGGER_2] Emparejar los cuatro pares; a y D²f son simétricas.
        self.play(FadeIn(a), FadeIn(hessian), Write(matrix_names))
        for k in range(4):
            self.play(Indicate(a.get_entries()[k], color=ACCENT_MINT),
                      Indicate(hessian.get_entries()[k], color=ACCENT_MINT), run_time=.65)
        contraction = stack(math(r"dX_i\,dX_j=a_{ij}\,dt", 34, ACCENT_CYAN),
                            math(r"\frac12\sum_{i,j}a_{ij}f_{x_ix_j}", 34),
                            math(r"=\frac12\operatorname{tr}(aD^2f)", 34, ACCENT_MINT),
                            center=RIGHT*3.15+UP*.4)
        self.play(ReplacementTransform(taylor, contraction), run_time=2)
        self.wait(4)
        # [TRIGGER_3] La fórmula completa se escribe en renglones legibles.
        final = stack(math(r"df(t,X_t)=", 36),
                      math(r"\bigl[f_t+\nabla f^\top b", 36),
                      math(r"{}+\frac12\operatorname{tr}(aD^2f)\bigr]dt", 36),
                      math(r"{}+\nabla f^\top G\,dB_t", 36, ACCENT_CYAN),
                      math(r"a=GG^\top,\qquad f\in C^{1,2}", 30),
                      center=RIGHT*3.15, buff=.38)
        # Cada renglón es LaTeX independiente: no dejamos delimitadores sin pareja.
        self.play(FadeOut(contraction))
        for row in final:
            self.play(Write(row))
        self.play(Circumscribe(final[2], color=ACCENT_MINT))
        conclusion(self, "Todas las curvaturas se ponderan por la covarianza instantánea.")
