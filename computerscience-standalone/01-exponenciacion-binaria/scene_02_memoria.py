from manim import *
import numpy as np
from scene_utils import *


class Escena02Memoria(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG_COLOR
        self.add(heading(2, "Un número enorme, un límite concreto"))
        # [TRIGGER_1] Dígitos ilustrativos, no expansión decimal real.
        digits = VGroup(*[formula("314159265358979323846264338327950288419716939937510", 22, TEXT_MUTED) for _ in range(3)]).arrange(DOWN, buff=0.12).move_to(UP * 1.55)
        self.play(FadeIn(digits), run_time=1)
        self.play(digits.animate.shift(LEFT * 0.4), run_time=2)
        # [TRIGGER_2] floor(n log10(3)) + 1.
        total = card("3 elevado a un millón", "477 122 dígitos", COLOR_EXPOS).move_to(LEFT * 3 + DOWN * 0.5)
        self.play(FadeIn(total))
        # [TRIGGER_3] Motivo astronómico para comparar magnitudes.
        universe = Circle(radius=0.65, color=COLOR_CYAN).move_to(RIGHT * 3 + DOWN * 0.25)
        stars = VGroup(*[Dot(universe.get_center() + 0.45 * np.array([np.cos(t), np.sin(t), 0]), radius=0.035, color=COLOR_CYAN) for t in np.linspace(0, TAU, 7)[:-1]])
        self.play(Create(universe), FadeIn(stars))
        # [TRIGGER_4] Comparar magnitudes no demuestra imposibilidad de almacenaje.
        atoms = formula(r"10^{80}\;\text{átomos (aprox.)}", 28, COLOR_CYAN).next_to(universe, DOWN, buff=0.2)
        self.play(Write(atoms))
        self.wait(1)
        self.play(FadeOut(VGroup(universe, stars, atoms)))
        # [TRIGGER_5] Overflow de un tipo fijo, no de toda la RAM.
        chip = card("Entero de 64 bits", "NO CABE", COLOR_FORCE_BRUTE).move_to(RIGHT * 3 + DOWN * 0.5)
        self.play(FadeIn(chip), Circumscribe(total, color=COLOR_EXPOS))
        note = VGroup(label("Sí se puede almacenar con enteros de precisión arbitraria.", 25), label("Representación binaria: aproximadamente 194 KiB de datos.", 22, COLOR_OPTIMAL)).arrange(DOWN, buff=0.2).move_to(DOWN * 2.4)
        self.play(FadeIn(note))
        self.wait(3)
