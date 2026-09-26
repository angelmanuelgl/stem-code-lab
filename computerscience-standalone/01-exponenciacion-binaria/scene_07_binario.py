from manim import *
from scene_utils import *


class Escena07Binario(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG_COLOR
        self.add(heading(7, "Los bits eligen las potencias"))
        # [TRIGGER_1] Decimal.
        decimal = formula("25", 65).move_to(UP * 1.9)
        self.play(Write(decimal))
        # [TRIGGER_2] Descomposición única para enteros no negativos.
        decomposition = formula("25=16+8+1", 45).move_to(UP * 1.9)
        self.play(ReplacementTransform(decimal, decomposition))
        # [TRIGGER_3] Las cinco posiciones binarias.
        bits = bit_row().move_to(UP * 0.6)
        self.play(LaggedStart(*[FadeIn(cell) for cell in bits], lag_ratio=0.15))
        # [TRIGGER_4] Pesos correspondientes a cada bit.
        weights = VGroup(*[formula(str(n), 26, COLOR_OPTIMAL if b == "1" else TEXT_MUTED).next_to(cell, DOWN, buff=0.2) for n, b, cell in zip([16, 8, 4, 2, 1], "11001", bits)])
        self.play(FadeIn(weights))
        for i in [0, 1, 4]:
            self.play(bits[i][0].animate.set_stroke(COLOR_OPTIMAL).set_fill(COLOR_OPTIMAL, 0.15), run_time=0.4)
        # [TRIGGER_5] La suma de exponentes se convierte en producto.
        product = MathTex(r"3^{25}=", r"3^{16}", r"\cdot", r"3^8", r"\cdot", r"3^1", font_size=49, color=TEXT_MAIN).move_to(DOWN * 1.55)
        self.play(Write(product))
        # [TRIGGER_6] Correspondencia entre bits activos y factores.
        boxes = VGroup(*[SurroundingRectangle(product[i], color=COLOR_EXPOS, buff=0.12) for i in [1, 3, 5]])
        self.play(Create(boxes))
        self.play(FadeIn(label("Bit 1: multiplicar  ·  Bit 0: omitir", 25, COLOR_OPTIMAL).to_edge(DOWN, buff=0.55)))
        self.wait(3)
