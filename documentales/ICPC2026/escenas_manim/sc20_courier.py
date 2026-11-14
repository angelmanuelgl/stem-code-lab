"""Bloque 2: enunciado y conteo riguroso de rutas en Clumsy Courier."""
from manim import *
from base_theme import BaseScene, label, formula, grid_graph, card
from theme import TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT, ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN


class EnunciadoCourier(BaseScene):
    """Resumen del enunciado en cuatro láminas legibles, con mini mapa persistente."""
    PANELS = [
        ("Problem C — Clumsy Courier",
         "R calles horizontales; C calles verticales.\nInicio: (1,1). Entrega: (R,C)."),
        ("Movimientos y límites",
         "Down: (r+1,c)   Up: (r-1,c)\nRight: (r,c+1)   Left: (r,c-1)\nCada movimiento sigue una arista de la cuadrícula."),
        ("Desvíos obligatorios",
         "Exactamente U movimientos Up\ny exactamente L movimientos Left.\nSe permite visitar vértices repetidos."),
        ("Qué se debe contar",
         "Secuencias distintas de movimientos\nque terminan en (R,C) y permanecen en la malla.\nR,C max 2000; U,L max 2000.\nResultado módulo 998,244,353."),
    ]

    def construct(self):
        mini, points = grid_graph(1, 1, cell=1.08)
        offset = RIGHT * 4.35 + DOWN * 0.15
        mini.shift(offset)
        points = {key: point + offset for key, point in points.items()}
        start = Dot(points[(0, 0)], radius=0.09, color=ACCENT_MINT)
        goal = Dot(points[(1, 1)], radius=0.09, color=ACCENT_VINO)
        persistent = VGroup(mini, start, goal)

        heading, copy = self.PANELS[0]
        title = self.title(heading)
        frame = RoundedRectangle(width=7.1, height=3.1, corner_radius=0.1,
                                 color=ACCENT_CYAN, stroke_width=2.2)
        frame.move_to(LEFT * 2.4 + DOWN * 0.15)
        body = label(copy, 25, TEXT_MAIN, width=6.25).move_to(frame)
        page = formula(r"1/4", 22, TEXT_MUTED).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(title), Create(frame), FadeIn(body), Create(persistent), FadeIn(page), run_time=1.0)
        self.wait(3.0)
        for i, (heading, copy) in enumerate(self.PANELS[1:], 2):
            next_title = self.title(heading)
            next_body = label(copy, 25, TEXT_MAIN, width=6.25).move_to(frame)
            next_page = formula(rf"{i}/4", 22, TEXT_MUTED).to_edge(DOWN, buff=0.3)
            self.play(Transform(title, next_title), Transform(body, next_body),
                      Transform(page, next_page), run_time=0.85)
            self.wait(3.0)
        self.wait(1.0)

class TraduccionCourier(BaseScene):
    def construct(self):
        self.play(Write(self.title("Traducir la historia a movimientos")))
        grid, points = grid_graph(1, 1, cell=1.55, color=ACCENT_CYAN)
        offset = LEFT * 2.6 + DOWN * 0.15
        grid.shift(offset)
        points = {k: v + offset for k, v in points.items()}
        start, goal = Dot(points[(0, 0)], color=ACCENT_MINT, radius=0.1), Dot(points[(1, 1)], color=ACCENT_VINO, radius=0.1)
        self.play(Create(grid), FadeIn(start), FadeIn(goal), run_time=1.0)
        coord_labels = VGroup(
            formula(r"(1,1)", 25, ACCENT_MINT).next_to(start, UL, buff=0.15),
            formula(r"(R,C)", 25, ACCENT_VINO).next_to(goal, DR, buff=0.15),
        )
        self.play(FadeIn(coord_labels), run_time=0.6)
        base_path = VMobject(color=ACCENT_CYAN, stroke_width=4).set_points_as_corners(
            [points[(0, 0)], points[(0, 1)], points[(1, 1)]])
        self.play(Create(base_path), run_time=1.0)
        base_label = label("avance base: Right y Down", 24, ACCENT_CYAN).move_to(RIGHT * 2.5 + UP * 1.0)
        self.play(FadeIn(base_label), run_time=0.6)
        detours = VGroup(
            Arrow(RIGHT * 1.0 + DOWN * 0.1, RIGHT * 1.0 + UP * 1.25,
                  color=ACCENT_TERRACOTTA, buff=0.05),
            Arrow(LEFT * 2.6 + DOWN * 0.2, RIGHT * 0.2 + DOWN * 0.2,
                  color=ACCENT_INDIGO, buff=0.05),
        )
        counts = VGroup(formula(r"U=0", 28, ACCENT_TERRACOTTA),
                        formula(r"L=0", 28, ACCENT_INDIGO)).arrange(RIGHT, buff=0.75)
        counts.move_to(RIGHT * 2.55 + DOWN * 0.25)
        self.play(Create(detours), FadeIn(counts), run_time=0.9)
        note = label("los vértices pueden repetirse", 22, TEXT_MUTED).move_to(RIGHT * 2.55 + DOWN * 1.15)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.8)


class CourierBase2x2(BaseScene):
    ROUTES = ["RD", "DR"]

    def construct(self):
        self.play(Write(self.title("Caso base: U=0, L=0")))
        grid, points = grid_graph(1, 1, cell=2.15, color=ACCENT_CYAN)
        offset = LEFT * 3.15 + DOWN * 0.15
        grid.shift(offset)
        points = {k: v + offset for k, v in points.items()}
        start = Dot(points[(0, 0)], color=ACCENT_MINT, radius=0.1)
        goal = Dot(points[(1, 1)], color=ACCENT_VINO, radius=0.1)
        params = VGroup(formula(r"2\times2", 28, TEXT_MAIN),
                        formula(r"U=0,\quad L=0", 25, ACCENT_INDIGO))
        params.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(RIGHT * 3.1 + UP * 1.1)
        counter = formula(r"N=0", 39, ACCENT_MINT).move_to(RIGHT * 3.1 + DOWN * 0.1)
        self.play(Create(grid), FadeIn(start), FadeIn(goal), FadeIn(params), FadeIn(counter), run_time=1.0)
        self.wait(0.9)
        for count, sequence in enumerate(self.ROUTES, 1):
            coords = self._coordinates(sequence)
            route = VMobject(color=ACCENT_MINT, stroke_width=4.4).set_points_as_corners([points[p] for p in coords])
            courier = Dot(points[(0, 0)], color=ACCENT_TERRACOTTA, radius=0.1)
            seq = formula(r"\text{ruta: }" + r"\to ".join(sequence), 25, ACCENT_CYAN)
            seq.move_to(RIGHT * 3.1 + DOWN * 1.2)
            next_count = formula(rf"N={count}", 39, ACCENT_MINT).move_to(counter)
            self.play(Create(route), FadeIn(courier), FadeIn(seq), run_time=0.7)
            self.play(MoveAlongPath(courier, route), run_time=1.45, rate_func=linear)
            self.play(Transform(counter, next_count), run_time=0.65)
            self.wait(0.9)
            self.play(FadeOut(route), FadeOut(courier), FadeOut(seq), run_time=0.45)
        summary_title = label("secuencias válidas", 20, ACCENT_CYAN).move_to(RIGHT * 3.1 + DOWN * 0.9)
        summary = VGroup(*[formula(r"\to ".join(path), 23, TEXT_MAIN) for path in self.ROUTES])
        summary.arrange(DOWN, buff=0.16).move_to(RIGHT * 3.1 + DOWN * 1.8)
        self.play(FadeIn(summary_title), FadeIn(summary), run_time=0.8)
        self.wait(1.7)

    @staticmethod
    def _coordinates(sequence):
        coords = [(0, 0)]
        for move in sequence:
            r, c = coords[-1]
            coords.append((r + (move == "D") - (move == "U"), c + (move == "R") - (move == "L")))
        return coords

class CourierOneUp(BaseScene):
    ROUTES = ["RDUD", "DRUD", "DURD", "DUDR"]

    def construct(self):
        self.play(Write(self.title("Un movimiento Up y ningún Left")))
        grid, points = grid_graph(1, 1, cell=2.15, color=ACCENT_CYAN)
        offset = LEFT * 3.15 + DOWN * 0.15
        grid.shift(offset)
        points = {k: v + offset for k, v in points.items()}
        start = Dot(points[(0, 0)], color=ACCENT_MINT, radius=0.1)
        goal = Dot(points[(1, 1)], color=ACCENT_VINO, radius=0.1)
        params = VGroup(formula(r"U=1", 32, ACCENT_TERRACOTTA),
                        formula(r"L=0", 32, ACCENT_INDIGO)).arrange(RIGHT, buff=0.75)
        params.move_to(RIGHT * 3.05 + UP * 1.0)
        counter = formula(r"N=0", 39, ACCENT_MINT).move_to(RIGHT * 3.05 + DOWN * 0.05)
        sequence_slot = RIGHT * 3.05 + DOWN * 1.1
        self.play(Create(grid), FadeIn(start), FadeIn(goal), FadeIn(params), FadeIn(counter), run_time=1.0)
        self.wait(1.0)
        for i, route_text in enumerate(self.ROUTES, 1):
            coords = CourierBase2x2._coordinates(route_text)
            route = VMobject(color=ACCENT_MINT, stroke_width=4.2).set_points_as_corners([points[p] for p in coords])
            courier = Dot(points[(0, 0)], color=ACCENT_TERRACOTTA, radius=0.1)
            seq = formula(r"\text{ruta: }" + r"\to ".join(route_text), 26, TEXT_MAIN).move_to(sequence_slot)
            new_count = formula(rf"N={i}", 39, ACCENT_MINT).move_to(counter)
            self.play(Create(route), FadeIn(courier), FadeIn(seq), run_time=0.7)
            self.play(MoveAlongPath(courier, route), run_time=1.35, rate_func=linear)
            self.play(Transform(counter, new_count), run_time=0.65)
            self.wait(0.8)
            self.play(FadeOut(route), FadeOut(courier), FadeOut(seq), run_time=0.4)
        summary_title = label("cuatro secuencias válidas", 20, ACCENT_CYAN)
        summary_title.move_to(RIGHT * 3.05 + DOWN * 0.95)
        summary = VGroup(*[
            formula(r"\to ".join(route_text), 21, TEXT_MAIN)
            for route_text in self.ROUTES
        ]).arrange(DOWN, buff=0.12)
        summary.move_to(RIGHT * 3.05 + DOWN * 1.85)
        self.play(FadeIn(summary_title), FadeIn(summary), run_time=0.8)
        self.wait(2.0)

class CourierEscala(BaseScene):
    def construct(self):
        self.play(Write(self.title("A gran escala: contar sin enumerar")))
        small, _ = grid_graph(1, 1, cell=0.82, color=ACCENT_CYAN)
        small.move_to(LEFT * 4.8 + DOWN * 0.2)
        small_tag = formula(r"2\times2", 23, TEXT_MAIN).next_to(small, DOWN, buff=0.25)
        self.play(Create(small), FadeIn(small_tag), run_time=0.8)
        big, _ = grid_graph(6, 8, cell=0.43, color=TEXT_MUTED)
        big.move_to(LEFT * 0.7 + DOWN * 0.1)
        big_tag = formula(r"R\times C", 25, TEXT_MAIN).next_to(big, DOWN, buff=0.2)
        self.play(Transform(small, big), Transform(small_tag, big_tag), run_time=1.4)
        params = VGroup(formula(r"U", 30, ACCENT_TERRACOTTA),
                        formula(r"L", 30, ACCENT_INDIGO)).arrange(RIGHT, buff=0.4)
        count = formula(r"N_{\text{rutas}}", 30, ACCENT_MINT)
        processor = VGroup(Circle(radius=0.55, color=ACCENT_MINT, stroke_width=2.4),
                           formula(r"\Sigma", 31, ACCENT_MINT))
        processor[1].move_to(processor[0])
        stack = VGroup(params, processor, count).arrange(DOWN, buff=0.65).move_to(RIGHT * 4.6 + DOWN * 0.1)
        self.play(FadeIn(params), run_time=0.6)
        self.play(FadeIn(processor), run_time=0.8)
        self.play(FadeIn(count), run_time=0.7)
        self.wait(2.0)
