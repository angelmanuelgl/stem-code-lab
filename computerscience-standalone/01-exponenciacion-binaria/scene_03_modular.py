from manim import *
import numpy as np
from scene_utils import *


class Escena03Modular(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG_COLOR
        # [TRIGGER_1] Introducción al módulo.
        self.play(FadeIn(heading(3, "Aritmética modular: dar la vuelta")))
        center = LEFT * 3 + DOWN * 0.1
        dial = Circle(radius=1.65, color=COLOR_MODULO).move_to(center)
        numbers = VGroup(*[formula(str(i), 24).move_to(center + 1.37 * np.array([np.sin(i * TAU / 12), np.cos(i * TAU / 12), 0])) for i in range(12)])
        hand = Arrow(center, center + LEFT * 1.08, buff=0, color=COLOR_EXPOS)
        # [TRIGGER_2] Reloj con residuos 0 a 11.
        self.play(Create(dial), FadeIn(numbers), GrowArrow(hand))
        # [TRIGGER_3] Siete posiciones en sentido horario desde 9 hasta 4.
        for _ in range(7):
            self.play(Rotate(hand, angle=-TAU / 12, about_point=center), run_time=0.35)
        equation = formula(r"(9+7)\bmod 12=4", 40).move_to(RIGHT * 2.9 + UP * 0.6)
        self.play(Write(equation))
        # [TRIGGER_4] Generalización del tamaño del reloj.
        modulus = formula(r"M=10^9+7", 40, COLOR_CYAN).move_to(center)
        self.play(FadeOut(hand), FadeOut(numbers), ReplacementTransform(dial, SurroundingRectangle(modulus, color=COLOR_MODULO, buff=0.35)), Write(modulus))
        # [TRIGGER_5] Productos seguros si ambos factores ya están reducidos.
        safe = VGroup(formula(r"0\leq A,B<M", 31), formula(r"AB<M^2<2^{63}-1", 31, COLOR_OPTIMAL)).arrange(DOWN, buff=0.35).move_to(RIGHT * 2.9 + DOWN * 1.05)
        self.play(Write(safe), Create(SurroundingRectangle(safe, color=COLOR_OPTIMAL, buff=0.25)))
        self.play(FadeIn(label("Calculamos el residuo; no el entero completo.", 26, COLOR_CYAN).to_edge(DOWN, buff=0.55)))
        self.wait(3)
