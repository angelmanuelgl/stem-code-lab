from manim import *
from scene_utils import *


class Escena01Gancho(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG_COLOR
        self.add(heading(1, "Un millón en el exponente"))
        # [TRIGGER_1] Presentación del reto.
        power = MathTex("3", r"^{1\,000\,000}", font_size=86, color=TEXT_MAIN).move_to(UP * 1.3)
        power[0].set_color(COLOR_MODULO)
        power[1].set_color(COLOR_EXPOS)
        self.play(Write(power), run_time=2)
        # [TRIGGER_2] Una iteración por bit; no una multiplicación por bit.
        fast = card("Exponenciación binaria", "20 iteraciones", COLOR_OPTIMAL).move_to(RIGHT * 3 + DOWN)
        self.play(FadeIn(fast, scale=0.6))
        # [TRIGGER_3] Método que comienza con resultado = 3.
        slow = card("Método ingenuo", "", COLOR_FORCE_BRUTE).move_to(LEFT * 3 + DOWN)
        count = Integer(0, mob_class=MathTex, font_size=40, color=TEXT_MAIN).move_to(LEFT * 3 + DOWN * 1.2)
        track = Rectangle(width=4.5, height=0.14, stroke_width=0, fill_color=TEXT_MUTED, fill_opacity=0.4).move_to(LEFT * 3 + DOWN * 2.15)
        bar = track.copy().set_fill(COLOR_FORCE_BRUTE, 1).stretch_to_fit_width(0.01).align_to(track, LEFT)
        self.play(FadeIn(slow), FadeIn(count), FadeIn(track), FadeIn(bar))
        self.play(ChangeDecimalToValue(count, 999999), bar.animate.stretch_to_fit_width(4.5).move_to(track), run_time=4)
        self.wait(1)
        # [TRIGGER_4] El reto y la promesa quedan en el centro.
        self.play(FadeOut(VGroup(slow, count, track, bar)), fast.animate.move_to(DOWN * 0.6))
        note = label("20 bits · 27 multiplicaciones en el código mostrado", 22, TEXT_MUTED).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(note))
        self.wait(2)
