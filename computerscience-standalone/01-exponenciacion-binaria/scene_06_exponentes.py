from manim import *
from scene_utils import *


class Escena06Exponentes(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG_COLOR
        self.add(heading(6, "¿Y si el exponente es 25?"))
        line = NumberLine(x_range=[0, 32, 4], length=11, color=TEXT_MUTED, include_numbers=False).move_to(DOWN * 1.5)
        self.play(Create(line))
        # [TRIGGER_1] Marcas proporcionales al valor, sin amontonar etiquetas.
        for i, n in enumerate([1, 2, 4, 8, 16, 32]):
            dot = Dot(line.n2p(n), color=COLOR_OPTIMAL)
            number = formula(str(n), 21, COLOR_OPTIMAL).move_to(line.n2p(n) + DOWN * (0.4 if i % 2 else 0.8))
            self.play(FadeIn(dot), FadeIn(number), run_time=0.4)
        # [TRIGGER_2] El objetivo no es una potencia de dos.
        target = Dot(line.n2p(25), color=COLOR_EXPOS)
        target_label = formula("25", 25, COLOR_EXPOS).next_to(target, DOWN)
        self.play(FadeIn(target), Write(target_label))
        # [TRIGGER_3] Exponente pendiente.
        power = formula(r"3^{25}=?", 70, COLOR_EXPOS).move_to(UP * 1.1)
        self.play(Write(power))
        # [TRIGGER_4] Duplicar 16 lleva a 32, no a 25.
        jump = CurvedArrow(line.n2p(16) + UP * 0.15, line.n2p(32) + UP * 0.15, angle=-PI / 2, color=COLOR_FORCE_BRUTE)
        self.play(Create(jump))
        explanation = formula(r"16\times2=32:\;\text{nos pasamos}", 23, COLOR_FORCE_BRUTE).move_to(UP * 0.25)
        self.play(FadeIn(explanation))
        # [TRIGGER_5] Abrir la puerta a la descomposición.
        self.play(FadeIn(label("¿Podemos sumar potencias de 2 para construir 25?", 27).to_edge(DOWN, buff=0.4)))
        self.wait(3)
