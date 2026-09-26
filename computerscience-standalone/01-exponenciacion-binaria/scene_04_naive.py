from manim import *
from scene_utils import *


class Escena04Naive(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG_COLOR
        self.add(heading(4, "Multiplicar de uno en uno"))
        # [TRIGGER_1] Ejemplo pequeño.
        power = formula(r"3^8", 64).move_to(UP * 1.9)
        self.play(Write(power))
        # [TRIGGER_2] Ocho factores y siete multiplicaciones.
        expanded = formula(r"3^8=3\times3\times3\times3\times3\times3\times3\times3", 38).move_to(UP * 1.9)
        self.play(ReplacementTransform(power, expanded))
        rows = VGroup(*[formula(rf"\text{{Paso {i}: }}3^{{{i+1}}}={3**(i+1)}", 28) for i in range(8)]).arrange_in_grid(rows=4, cols=2, buff=(1.6, 0.3)).move_to(DOWN * 0.25)
        # [TRIGGER_3] El valor inicial no requiere multiplicaciones.
        self.play(FadeIn(rows[0]))
        # [TRIGGER_4] Primera multiplicación.
        self.play(Write(rows[1]))
        # [TRIGGER_5] Acumular los seis pasos restantes.
        for row in rows[2:]:
            self.play(FadeIn(row, shift=UP * 0.1), run_time=0.6)
        # [TRIGGER_6] Relación entre n y el trabajo.
        self.play(Create(SurroundingRectangle(rows, color=COLOR_FORCE_BRUTE, buff=0.3)))
        result = formula(r"n-1\;\text{multiplicaciones}\quad\Longrightarrow\quad O(n)", 35, COLOR_FORCE_BRUTE).to_edge(DOWN, buff=0.55)
        self.play(Write(result))
        self.wait(3)
