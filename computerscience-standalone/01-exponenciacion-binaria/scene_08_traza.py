from manim import *
from scene_utils import *


class Escena08Traza(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG_COLOR
        self.add(heading(8, "Dentro del algoritmo"))
        bits = bit_row().move_to(UP * 1.7)
        # [TRIGGER_1] Paneles y lectura de derecha a izquierda.
        self.play(FadeIn(bits))
        mode = label("Cálculo módulo 1 000 000 007", 21, COLOR_CYAN).move_to(UP * 0.7)
        self.play(FadeIn(mode))
        # [TRIGGER_2] Estado inicial.
        res, base = 1, 3
        res_card = card("res · acumulador", str(res), COLOR_OPTIMAL, 4.7).move_to(LEFT * 3.3 + DOWN * 0.6)
        base_card = card("base · potencia actual", str(base), COLOR_MODULO, 4.7).move_to(LEFT * 3.3 + DOWN * 2.5)
        pointer = Triangle(color=COLOR_CYAN, fill_opacity=1).scale(0.12).next_to(bits[4], DOWN, buff=0.12)
        self.play(FadeIn(res_card), FadeIn(base_card), FadeIn(pointer))
        log = VGroup()
        # [TRIGGER_3] a [TRIGGER_7]: un bit por iteración; mismo orden que C++.
        for step, bit in enumerate(reversed("11001")):
            index = 4 - step
            self.play(pointer.animate.next_to(bits[index], DOWN, buff=0.12), Indicate(bits[index], color=COLOR_EXPOS), run_time=0.6)
            old_res, old_base = res, base
            if bit == "1":
                res = res * base % MODULUS
                operation = formula(rf"{old_res}\times {old_base}\bmod M={res}", 18)
            else:
                operation = label(f"Bit 0: res permanece en {res}", 18)
            base = base * base % MODULUS
            new_res = card("res · acumulador", str(res), COLOR_OPTIMAL, 4.7).move_to(res_card)
            new_base = card("base · potencia actual", str(base), COLOR_MODULO, 4.7).move_to(base_card)
            entry = VGroup(label(f"{step+1}. Peso {2**step} · bit {bit}", 22, COLOR_OPTIMAL if bit == "1" else TEXT_MUTED), operation).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
            if entry.width > 5.3:
                entry.scale_to_fit_width(5.3)
            entry.move_to(RIGHT * 3 + UP * (0.05 - step * 0.68))
            log.add(entry)
            self.play(Transform(res_card, new_res), Transform(base_card, new_base), FadeIn(entry))
            self.wait(1)
        # [TRIGGER_8] Cinco iteraciones; ocho multiplicaciones con el último cuadrado.
        self.play(FadeOut(pointer), Circumscribe(res_card, color=COLOR_OPTIMAL))
        self.play(Transform(mode, label("5 iteraciones · 8 multiplicaciones · residuo: 288 603 514", 23, COLOR_OPTIMAL).move_to(mode)))
        self.wait(3)
