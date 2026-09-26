from manim import *
from scene_utils import *


class Escena05Intuicion(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG_COLOR
        self.add(heading(5, "Reutilizar: duplicar el exponente"))
        nodes = VGroup(*[VGroup(formula(rf"3^{{{e}}}", 48, COLOR_MODULO), formula(str(3**e), 25)).arrange(DOWN, buff=0.3) for e in [1, 2, 4, 8]]).arrange(RIGHT, buff=1.5)
        # [TRIGGER_1] Partimos de la base.
        self.play(FadeIn(nodes[0]))
        # [TRIGGER_2], [TRIGGER_3], [TRIGGER_4]: cuadrados sucesivos.
        for i in range(1, 4):
            arrow = CurvedArrow(nodes[i-1].get_top() + UP * 0.2, nodes[i].get_top() + UP * 0.2, angle=-PI / 3, color=COLOR_OPTIMAL)
            square = formula(r"x^2", 25, COLOR_OPTIMAL).next_to(arrow, UP, buff=0.12)
            self.play(Create(arrow), Write(square))
            self.play(TransformFromCopy(nodes[i-1], nodes[i]))
            self.wait(0.7)
        # [TRIGGER_5] Comparación con el mismo objetivo: 3^8.
        summary = card("7 multiplicaciones → 3 multiplicaciones", "57 % menos", COLOR_OPTIMAL, width=7).move_to(DOWN * 2.15)
        self.play(FadeIn(summary, shift=UP * 0.2))
        self.wait(3)
