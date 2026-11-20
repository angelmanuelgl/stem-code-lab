"""Bloque 3: embudo de clasificacion y tablero Top 25 rumbo al LATAM Championship."""
from manim import *
from base_theme import BaseScene
from theme import (
    BG_COLOR,
    TEXT_MAIN,
    TEXT_MUTED,
    ACCENT_VINO,
    ACCENT_MINT,
    ACCENT_TERRACOTTA,
    ACCENT_INDIGO,
    ACCENT_CYAN,
)


class EmbudoClasificacion(BaseScene):
    def construct(self):
        # Tres niveles conectados: 509 -> 85 -> 20
        stages_data = [
            {
                "count": r"\textbf{509}",
                "title": r"\textbf{Equipos}",
                "sub": r"Tres fechas clasificatorias",
                "color": ACCENT_INDIGO,
                "width": 3.45,
                "height": 3.60,
                "pos": LEFT * 4.35,
            },
            {
                "count": r"\textbf{85}",
                "title": r"\textbf{Finalistas}",
                "sub": r"Gran final presencial",
                "color": ACCENT_CYAN,
                "width": 3.25,
                "height": 2.65,
                "pos": ORIGIN,
            },
            {
                "count": r"\textbf{20}",
                "title": r"\textbf{Medallistas}",
                "sub": r"Podio nacional ICPC",
                "color": ACCENT_MINT,
                "width": 3.05,
                "height": 1.95,
                "pos": RIGHT * 4.35,
            },
        ]

        cards = []
        for item in stages_data:
            box = RoundedRectangle(
                width=item["width"],
                height=item["height"],
                corner_radius=0.16,
                stroke_color=item["color"],
                stroke_width=2.2,
                fill_color="#1E2430",
                fill_opacity=0.92,
            )
            num_tex = Tex(item["count"], font_size=46, color=item["color"])
            title_tex = Tex(item["title"], font_size=22, color=TEXT_MAIN)
            sub_tex = Tex(item["sub"], font_size=16, color=TEXT_MUTED)

            content = VGroup(num_tex, title_tex, sub_tex).arrange(DOWN, buff=0.14)
            if content.height > item["height"] - 0.35:
                content.scale_to_fit_height(item["height"] - 0.35)
            content.move_to(box.get_center())

            card_group = VGroup(box, content).move_to(item["pos"])
            cards.append(card_group)

        arrow_1_2 = Arrow(
            cards[0].get_right() + RIGHT * 0.10,
            cards[1].get_left() + LEFT * 0.10,
            buff=0.05,
            stroke_color=TEXT_MUTED,
            stroke_width=2.6,
            max_tip_length_to_length_ratio=0.22,
        )
        arrow_2_3 = Arrow(
            cards[1].get_right() + RIGHT * 0.10,
            cards[2].get_left() + LEFT * 0.10,
            buff=0.05,
            stroke_color=TEXT_MUTED,
            stroke_width=2.6,
            max_tip_length_to_length_ratio=0.22,
        )

        # Animación secuencial dejando pausas amplias y conservando siempre todas las etiquetas
        self.play(FadeIn(cards[0], shift=UP * 0.18), run_time=1.0)
        self.wait(1.2)

        self.play(
            GrowArrow(arrow_1_2),
            FadeIn(cards[1], shift=UP * 0.18),
            run_time=1.0,
        )
        self.wait(1.2)

        self.play(
            GrowArrow(arrow_2_3),
            FadeIn(cards[2], shift=UP * 0.18),
            run_time=1.0,
        )
        self.wait(2.2)

        # Animación de salida explícita para todo lo que entró
        self.play(
            FadeOut(cards[2], shift=DOWN * 0.15),
            FadeOut(arrow_2_3),
            FadeOut(cards[1], shift=DOWN * 0.15),
            FadeOut(arrow_1_2),
            FadeOut(cards[0], shift=DOWN * 0.15),
            run_time=1.0,
        )
        self.wait(0.3)


class TablaTop25Latam(BaseScene):
    def construct(self):
        # Datos exactos en el orden del listado fuente:
        # (rank_str, institucion_latex, equipo_latex, resueltos_str, avanzo_bool, es_guest)
        rows_data = [
            ("1", r"ESCOM IPN", r"Domain Expansion ``Abraham \'echate un hint''", "10", True, False),
            (" ", r"CCM", r"Chatcito, Claudecito y Geminicito - Campeones OMI 2026 [Invitado / Guest]", "10", False, True),
            ("2", r"U de Guanajuato", r"Soy malo y eso es bueno, yo jam\'as ser\'e bueno y eso no es malo", "9", True, False),
            ("3", r"UP GDL", r"Prisioneros de Alcatraz", "8", True, False),
            ("4", r"ITESM Monterrey", r"Academia de Pilotaje Aerost\'atico Manuel Doblado ...", "8", True, False),
            ("5", r"UP Bonaterra", r"The good, the bad and the ugly", "8", True, False),
            ("6", r"FC-UNAM", r"Oasis", "8", True, False),
            ("7", r"U de Guanajuato", r"ICAxiom", "8", True, False),
            ("8", r"IT Culiacan", r"Los guerreros m\'as fuertes de wkoder", "8", True, False),
            ("9", r"UADY", r"Gauss N' Roses", "8", True, False),
            ("10", r"UANL", r"No te preocupes, menci\'on honor\'ifica tambi\'en es buen resultado", "8", True, False),
            ("11", r"UADY", r"PEScapitalista", "8", True, False),
            ("12", r"Facultad de Ingenier\'ia UNAM", r":)", "8", True, False),
            ("13", r"UdG CUCEI", r"Adri\'an quer\'ia que nos pusi\'eramos un nombre largo por alguna raz\'on, y ...", "8", True, False),
            ("14", r"ITESM GDA", r"Hijos del Puntero", "7", True, False),
            ("15", r"UADY", r"Tuntunsitos", "7", False, False),
            ("16", r"ESCOM IPN", r"Las Chivas de Milito", "7", False, False),
            ("17", r"IT Culiacan", r"AD-HOCK", "7", False, False),
            ("18", r"U de Guanajuato", r"M\"athgic Cr\"ue", "7", False, False),
            ("19", r"FC-UNAM", r"Claude Opus 4.6", "7", False, False),
            ("20", r"ITESM Monterrey", r"Data Divas", "6", True, False),
            ("21", r"ITESM Monterrey", r"ATCSUSMS (Alianza)", "6", True, False),
            ("22", r"UAM A", r"Seal++", "6", True, False),
            ("23", r"UASLP", r"Tacos de Schnauzer", "6", True, False),
            ("24", r"UAEH", r"CapyBaby's", "6", True, False),
            ("25", r"Facultad de Ingenier\'ia UNAM", r"Alianza de Autismo de Puerto Rico", "6", False, False),
        ]

        # Geometría compacta y legible sin título superior (27 filas totales: encabezado + 26 equipos)
        col_widths = [0.85, 2.95, 7.25, 1.35]
        total_w = sum(col_widths)
        row_h = 0.232
        top_y = 3.55
        table_x_center = -0.35  # Ligero desplazamiento a la izquierda para dejar aire a las llaves derechas

        col_x = []
        cursor_x = table_x_center - total_w / 2
        for w in col_widths:
            col_x.append(cursor_x + w / 2)
            cursor_x += w

        # Encabezado de tabla
        header_bg = Rectangle(
            width=total_w,
            height=row_h + 0.03,
            fill_color="#232A38",
            fill_opacity=1.0,
            stroke_color=ACCENT_INDIGO,
            stroke_width=1.2,
        ).move_to([table_x_center, top_y, 0])

        headers_text = [
            r"\textbf{Puesto}",
            r"\textbf{Instituci\'on}",
            r"\textbf{Nombre}",
            r"\textbf{Resueltos}",
        ]
        header_labels = VGroup()
        for idx, h_str in enumerate(headers_text):
            lbl = Tex(h_str, font_size=14, color=ACCENT_CYAN)
            lbl.move_to([col_x[idx], top_y, 0])
            header_labels.add(lbl)

        header_group = VGroup(header_bg, header_labels)

        # Construcción de las 26 filas
        row_objects = []
        for i, (rk, inst, team, solved, advanced, is_guest) in enumerate(rows_data):
            y_pos = top_y - (i + 1) * row_h
            base_fill = "#1B202B" if i % 2 == 0 else "#181C24"

            row_bg = Rectangle(
                width=total_w,
                height=row_h,
                fill_color=base_fill,
                fill_opacity=0.95,
                stroke_color=TEXT_MUTED,
                stroke_width=0.35,
                stroke_opacity=0.25,
            ).move_to([table_x_center, y_pos, 0])

            txt_color = TEXT_MUTED if is_guest else TEXT_MAIN
            solved_color = TEXT_MUTED if is_guest else ACCENT_CYAN

            t_rk = Tex(rk, font_size=13, color=txt_color).move_to([col_x[0], y_pos, 0])

            t_inst = Tex(inst, font_size=12.5, color=txt_color)
            if t_inst.width > col_widths[1] - 0.18:
                t_inst.scale_to_fit_width(col_widths[1] - 0.18)
            t_inst.move_to([col_x[1] - col_widths[1] / 2 + 0.10, y_pos, 0], aligned_edge=LEFT)

            t_team = Tex(team, font_size=12.5, color=txt_color)

            if t_team.width > col_widths[2] - 0.22:
                t_team.scale_to_fit_width(col_widths[2] - 0.22)
            t_team.move_to([col_x[2] - col_widths[2] / 2 + 0.10, y_pos, 0], aligned_edge=LEFT)

            t_sol = Tex(rf"\textbf{{{solved}}}", font_size=13, color=solved_color).move_to([col_x[3], y_pos, 0])

            row_group = VGroup(row_bg, t_rk, t_inst, t_team, t_sol)
            row_objects.append({
                "group": row_group,
                "bg": row_bg,
                "texts": VGroup(t_rk, t_inst, t_team, t_sol),
                "base_fill": base_fill,
                "rank": rk,
                "advanced": advanced,
                "is_guest": is_guest,
                "y": y_pos,
            })

        all_rows_vg = VGroup(*[r["group"] for r in row_objects])

        # 1. Aparición de la tabla completa con tiempo holgado de lectura
        self.play(FadeIn(header_group), run_time=0.8)
        self.play(
            LaggedStart(*[FadeIn(r["group"], shift=UP * 0.04) for r in row_objects], lag_ratio=0.03),
            run_time=2.2,
        )
        self.wait(3.2)

        # 2. Resaltar en verde suave las filas de quienes avanzan (sin atenuar ni ocultar el resto)
        green_fill_anims = []
        for r in row_objects:
            if r["advanced"]:
                green_fill_anims.append(
                    r["bg"].animate.set_fill(ACCENT_MINT, opacity=0.22).set_stroke(ACCENT_MINT, width=0.6, opacity=0.45)
                )

        self.play(*green_fill_anims, run_time=4.0)
        self.wait(2.8)

        # 3. Foco tipo hover en filas 15-19 (índices 15..19 en rows_data, pues index 1 es '-')
        ranks_15_19 = {"15", "16", "17", "18", "19"}
        hover_15_19_box = SurroundingRectangle(
            VGroup(*[r["group"] for r in row_objects if r["rank"] in ranks_15_19]),
            color=ACCENT_TERRACOTTA,
            buff=0.02,
            stroke_width=2.0,
        )

        focus_15_19_anims = [Create(hover_15_19_box)]
        for r in row_objects:
            if r["rank"] in ranks_15_19:
                focus_15_19_anims.append(
                    r["bg"].animate.set_fill(ACCENT_TERRACOTTA, opacity=0.22)
                )
            else:
                focus_15_19_anims.append(r["texts"].animate.set_opacity(0.45))

        self.play(*focus_15_19_anims, run_time=0.9)
        self.wait(2.5)

        # Retirar el foco 15-19 antes del siguiente bloque
        reset_15_19_anims = [FadeOut(hover_15_19_box)]
        for r in row_objects:
            if r["rank"] in ranks_15_19:
                reset_15_19_anims.append(
                    r["bg"].animate.set_fill(r["base_fill"], opacity=0.95)
                )
            reset_15_19_anims.append(r["texts"].animate.set_opacity(1.0))

        self.play(*reset_15_19_anims, run_time=0.7)
        self.wait(1.2)

        # 4. Pausa adecuada -> foco tipo hover en filas 20-25 y comparación con 15-19 mediante llaves
        ranks_20_25 = {"20", "21", "22", "23", "24", "25"}
        rows_15_19_vg = VGroup(*[r["group"] for r in row_objects if r["rank"] in ranks_15_19])
        rows_20_25_vg = VGroup(*[r["group"] for r in row_objects if r["rank"] in ranks_20_25])

        hover_20_25_box = SurroundingRectangle(
            rows_20_25_vg,
            color=ACCENT_CYAN,
            buff=0.02,
            stroke_width=2.0,
        )

        # Llaves de comparación entre celdas de problemas y estatus (sin flechas de causalidad)
        right_edge_x = table_x_center + total_w / 2 + 0.08
        brace_15_19 = BraceBetweenPoints(
            [right_edge_x, rows_15_19_vg.get_bottom()[1], 0],
            [right_edge_x, rows_15_19_vg.get_top()[1], 0],
            direction=RIGHT,
            color=ACCENT_TERRACOTTA,
        )
        lbl_15_19 = Tex(
            r"\textbf{7 prob.}\\[-2pt]\scriptsize No avanza",
            font_size=13,
            color=ACCENT_TERRACOTTA,
        ).next_to(brace_15_19, RIGHT, buff=0.08)

        brace_20_25 = BraceBetweenPoints(
            [right_edge_x, rows_20_25_vg.get_bottom()[1], 0],
            [right_edge_x, rows_20_25_vg.get_top()[1], 0],
            direction=RIGHT,
            color=ACCENT_MINT,
        )
        lbl_20_25 = Tex(
            r"\textbf{6 prob.}\\[-2pt]\scriptsize 20--24 avanzan",
            font_size=13,
            color=ACCENT_MINT,
        ).next_to(brace_20_25, RIGHT, buff=0.08)

        compare_anims = [
            Create(hover_20_25_box),
            GrowFromCenter(brace_15_19),
            FadeIn(lbl_15_19),
            GrowFromCenter(brace_20_25),
            FadeIn(lbl_20_25),
        ]
        for r in row_objects:
            if r["rank"] in ranks_20_25 or r["rank"] in ranks_15_19:
                compare_anims.append(r["texts"].animate.set_opacity(1.0))
            else:
                compare_anims.append(r["texts"].animate.set_opacity(0.45))

        self.play(*compare_anims, run_time=1.0)
        self.wait(3.0)

        # Retirar ambos resaltados y llaves al final
        cleanup_compare_anims = [
            FadeOut(hover_20_25_box),
            FadeOut(brace_15_19),
            FadeOut(lbl_15_19),
            FadeOut(brace_20_25),
            FadeOut(lbl_20_25),
        ]
        for r in row_objects:
            cleanup_compare_anims.append(r["texts"].animate.set_opacity(1.0))

        self.play(*cleanup_compare_anims, run_time=0.8)
        self.wait(0.8)

        # 5. Texto discreto abajo que se integre ligeramente con el color del fondo
        footnote_tex = Tex(
            r"Otros equipos que tambi\'en clasificaron: "
            r"49. [FC-UNAM] Gatos Naranjosos (4 problemas), "
            r"54. [Facultad de Ingenier\'ia UNAM] K-Pop Demon Coders (4 problemas), "
            r"55. [ITESM Monterrey] Sopes (3 problemas)",
            font_size=13,
            color=TEXT_MUTED,
        )
        footnote_tex.set_opacity(0.55)
        if footnote_tex.width > 13.0:
            footnote_tex.scale_to_fit_width(13.0)
        footnote_tex.to_edge(DOWN, buff=0.22)

        self.play(FadeIn(footnote_tex, shift=UP * 0.08), run_time=1.0)
        self.wait(3.0)

        # 6. Animación de salida explícita de todos los elementos
        self.play(
            FadeOut(footnote_tex, shift=DOWN * 0.1),
            FadeOut(all_rows_vg, shift=DOWN * 0.12),
            FadeOut(header_group, shift=UP * 0.1),
            run_time=1.1,
        )
        self.wait(0.3)