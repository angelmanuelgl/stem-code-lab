"""Gancho de apertura, adaptado a theme.py."""
from manim import *
from base_theme import BaseScene, formula
from theme import BG_COLOR, TEXT_MAIN, ACCENT_VINO, ACCENT_TERRACOTTA


class Gancho(BaseScene):
    def construct(self):
        beats = [
            (r"5\ \text{HORAS}", ACCENT_TERRACOTTA),
            (r"3\ \text{PERSONAS}", TEXT_MAIN),
            (r"1\ \text{COMPUTADORA}", ACCENT_VINO),
        ]
        for expression, color in beats:
            item = formula(expression, 54, color)
            self.play(FadeIn(item, shift=0.15 * UP), run_time=0.8)
            self.wait(1.6)
            self.play(FadeOut(item, shift=0.1 * DOWN), run_time=0.65)
        final = VGroup(
            Tex(r"Y un conjunto de problemas", color=TEXT_MAIN, font_size=36),
            Tex(r"que nadie en el planeta", color=TEXT_MAIN, font_size=36),
            Tex(r"ha visto antes.", color=ACCENT_VINO, font_size=40),
        ).arrange(DOWN, buff=0.28)
        self.play(Write(final[0]), run_time=1.0)
        self.wait(0.6)
        self.play(Write(final[1]), run_time=1.0)
        self.wait(0.6)
        self.play(Write(final[2]), run_time=1.1)
        self.wait(2.2)
        self.play(FadeOut(final), run_time=0.75)
