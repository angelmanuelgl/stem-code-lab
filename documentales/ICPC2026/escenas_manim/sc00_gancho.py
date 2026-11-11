from manim import *


class Gancho(Scene):
    """Apertura breve y tensa: escala de tiempo, equipo y computadora."""

    def construct(self):
        self.camera.background_color = BLACK
        beats = [
            (r"5\ \text{HORAS}", 1.05),
            (r"3\ \text{PERSONAS}", 1.00),
            (r"1\ \text{COMPUTADORA}", 0.86),
        ]
        for text, hold in beats:
            title = MathTex(text, color=WHITE).scale(1.1)
            self.play(FadeIn(title, shift=0.18 * UP), run_time=0.45)
            self.wait(hold)
            self.play(FadeOut(title, shift=0.12 * DOWN), run_time=0.35)

        final = VGroup(
            Tex(r"Y un conjunto de problemas", color=WHITE),
            Tex(r"que nadie en el planeta", color=WHITE),
            Tex(r"ha visto antes.", color=WHITE),
        ).arrange(DOWN, buff=0.22).scale(0.78)
        self.play(Write(final[0]), run_time=0.8)
        self.wait(0.35)
        self.play(Write(final[1]), run_time=0.8)
        self.play(Write(final[2]), run_time=0.65)
        self.wait(1.5)
        self.play(FadeOut(final), run_time=0.5)
