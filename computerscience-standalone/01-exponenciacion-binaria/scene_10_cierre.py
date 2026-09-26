from manim import *
from scene_utils import *


class Escena10Cierre(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG_COLOR
        title = heading(10, "Un exponente gigante, solo 20 bits")
        self.add(title)
        # [TRIGGER_1] Resolver la pregunta inicial con el residuo real.
        result = formula(rf"3^{{1\,000\,000}}\bmod(10^9+7)={pow(3, 1000000, MODULUS)}", 42).move_to(DOWN * 0.45)
        self.play(Write(result), run_time=2)
        # [TRIGGER_2] n-1 multiplicaciones partiendo de la base.
        slow = card("Método ingenuo", "999 999 multiplicaciones", COLOR_FORCE_BRUTE).move_to(LEFT * 3 + UP * 1.2)
        self.play(FadeIn(slow))
        # [TRIGGER_3] Comparación homogénea y número de iteraciones explícito.
        fast = card("Binaria · 20 iteraciones", "27 multiplicaciones", COLOR_OPTIMAL).move_to(RIGHT * 3 + UP * 1.2)
        self.play(FadeIn(fast), Circumscribe(fast, color=COLOR_OPTIMAL))
        takeaway = label("Eleva al cuadrado. Lee los bits. Combina.", 30, COLOR_EXPOS).move_to(DOWN * 1.8)
        self.play(Write(takeaway))
        self.wait(3)
        # [TRIGGER_4] Cierre legible que también sirve de fotograma final.
        self.play(FadeOut(VGroup(title, result, slow, fast, takeaway)))
        end = VGroup(label("Los algoritmos cambian la escala.", 40), label("Suscríbete para más algoritmos explicados visualmente", 25, COLOR_OPTIMAL), label("STEM CODE LAB", 20, COLOR_CYAN)).arrange(DOWN, buff=0.6)
        self.play(FadeIn(end, shift=UP * 0.2))
        self.wait(3)
