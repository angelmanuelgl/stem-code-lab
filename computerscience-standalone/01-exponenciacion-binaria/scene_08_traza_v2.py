from manim import *
from scene_utils import *


class Escena08TrazaV2(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG_COLOR
        self.add(heading(8, "Dentro del algoritmo"))

        # 1. Parámetros del número a evaluar
        # 1011001011₂ = 512 + 128 + 64 + 8 + 2 + 1 = 715
        binary_str = "1011001011"
        exponent_dec = int(binary_str, 2)  # 715
        n_bits = len(binary_str)

        # Fila de bits
        bits = bit_row(binary_str).move_to(UP * 1.8) if callable(bit_row) else bit_row().move_to(UP * 1.8)
        self.play(FadeIn(bits))

        # Indicación del número en decimal y binario usando Tex nativo
        mode = Tex(
            rf"Cálculo de $3^{{{exponent_dec}}} \bmod M$ \quad | \quad ${exponent_dec} = {binary_str}_2$",
            font_size=20 * 1.5,
            color=COLOR_CYAN
        ).move_to(UP * 0.9)
        self.play(FadeIn(mode))

        # 2. Tarjetas de estado inicial (ancho 5.8 para mantener fijo el título del acumulador)
        res_card = card("res · acumulador", "1", COLOR_OPTIMAL, 5.8).move_to(LEFT * 3.3 + DOWN * 0.5)
        base_card = card("base · potencia actual", "3^1", COLOR_MODULO, 5.8).move_to(LEFT * 3.3 + DOWN * 2.3)

        # Puntero en el LSB (índice n_bits - 1)
        pointer = Triangle(color=COLOR_CYAN, fill_opacity=1).scale(0.12).next_to(bits[n_bits - 1], DOWN, buff=0.12)
        self.play(FadeIn(res_card), FadeIn(base_card), FadeIn(pointer))

        used_powers = []
        current_step_panel = None  # Contenedor para el panel lateral único

        # 3. Iteración de derecha a izquierda
        for step, bit in enumerate(reversed(binary_str)):
            index = (n_bits - 1) - step
            power_val = 2**step  # 1, 2, 4, 8, 16, 32, 64, 128, 256, 512

            # (A) Mover puntero al bit actual
            self.play(
                pointer.animate.next_to(bits[index], DOWN, buff=0.12),
                Indicate(bits[index], color=COLOR_EXPOS),
                run_time=0.4
            )

            # (B) Panel explicativo del paso (se limpia el paso anterior)
            step_title = label(
                f"Paso {step+1} de {n_bits} · Peso {power_val} (bit {bit})", 
                17, 
                COLOR_OPTIMAL if bit == "1" else TEXT_MUTED
            )

            if bit == "1":
                step_op = Tex(
                    rf"Bit 1: res $\leftarrow$ res $\times 3^{{{power_val}}}$",
                    font_size=16 * 1.5,
                    color=COLOR_OPTIMAL
                )
            else:
                step_op = label("Bit 0: res no cambia", 16, TEXT_MUTED)

            new_step_panel = VGroup(step_title, step_op).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            new_step_panel.move_to(RIGHT * 3.2 + DOWN * 0.5)

            # Desvanecer el panel del paso anterior antes de mostrar el nuevo
            if current_step_panel is not None:
                self.play(FadeOut(current_step_panel), run_time=0.2)

            self.play(FadeIn(new_step_panel), run_time=0.3)
            current_step_panel = new_step_panel
            self.wait(0.8)  # Pausa tras explicar el paso

            # (C) Actualización del Acumulador (res)
            if bit == "1":
                used_powers.append(power_val)
                res_str = " · ".join([f"3^{p}" for p in used_powers])
                
                new_res_card = card("res · acumulador", res_str, COLOR_OPTIMAL, 5.8).move_to(res_card)
                self.play(Transform(res_card, new_res_card), run_time=0.5)
                self.wait(0.8)  # Pausa tras actualizar acumulador

            # (D) Actualización de la Potencia Base (base)
            next_power_val = 2**(step + 1)
            base_str = f"3^{{{next_power_val}}}"   # genera 3^{128}, no 3^128
            new_base_card = card("base · potencia actual", base_str, COLOR_MODULO, 5.8).move_to(base_card)

            self.play(Transform(base_card, new_base_card), run_time=0.5)
            self.wait(1.0)  # Pausa al finalizar el ciclo de elevación al cuadrado

        # Limpieza del panel lateral al concluir las iteraciones
        if current_step_panel is not None:
            self.play(FadeOut(current_step_panel), run_time=0.3)

        # 4. Estado Final
        self.play(FadeOut(pointer), Circumscribe(res_card, color=COLOR_OPTIMAL))

        powers_sum_str = " + ".join([f"{p}" for p in used_powers])
        final_summary = Tex(
            rf"Resultado: $3^{{{exponent_dec}}} = 3^{{{powers_sum_str}}}$",
            font_size=19 * 1.5,
            color=COLOR_OPTIMAL
        ).move_to(mode)

        self.play(Transform(mode, final_summary))
        self.wait(3)