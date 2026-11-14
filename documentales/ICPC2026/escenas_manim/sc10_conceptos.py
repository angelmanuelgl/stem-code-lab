"""Bloque 1: leer enunciados y administrar tiempo."""
from manim import *
from base_theme import BaseScene, card, label, formula
from theme import TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT, ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN


class EscuelaVsICPC(BaseScene):
    def construct(self):
        self.play(Write(self.title("Dos formas de leer un problema")))
        school = card("EJERCICIO ESCOLAR\nInstrucción directa\nTécnica sugerida", 4.7, 2.3, ACCENT_CYAN)
        contest = card("PROBLEMA ICPC\nHistoria\nTécnica desconocida", 4.7, 2.3, ACCENT_INDIGO)
        school.move_to(LEFT * 3.0 + DOWN * 0.15)
        contest.move_to(RIGHT * 3.0 + DOWN * 0.15)
        divider = DashedLine(UP * 2.0, DOWN * 1.5, color=TEXT_MUTED)
        toolbox = label("herramienta indicada", 22, ACCENT_CYAN).next_to(school, DOWN, buff=0.35)
        unknown = MathTex(r"?", color=ACCENT_TERRACOTTA, font_size=42).next_to(contest, DOWN, buff=0.23)
        self.play(Create(divider), FadeIn(school), FadeIn(contest), run_time=1.0)
        self.wait(0.8)
        self.play(FadeIn(toolbox), FadeIn(unknown), run_time=0.8)
        self.wait(1.3)
        self.play(Indicate(toolbox, color=ACCENT_CYAN), Indicate(unknown, color=ACCENT_TERRACOTTA), run_time=0.9)
        self.wait(1.6)


class PelarCebolla(BaseScene):
    def construct(self):
        self.play(Write(self.title("Quitar la historia; revelar la estructura")))
        story = card("Una historia\ncon datos y reglas", 5.0, 2.4, ACCENT_TERRACOTTA, 30)
        story.move_to(LEFT * 3.5 + DOWN * 0.25)
        arrow = Arrow(story.get_right(), RIGHT * 0.7 + DOWN * 0.25,
                      color=ACCENT_CYAN, stroke_width=2.5, buff=0.15)
        self.play(FadeIn(story), run_time=0.8)
        self.wait(0.7)
        self.play(GrowArrow(arrow), run_time=0.8)
        graph_shape = VGroup(
            Line(LEFT * 0.45, UP * 0.35, color=ACCENT_CYAN),
            Line(UP * 0.35, RIGHT * 0.55 + DOWN * 0.25, color=ACCENT_CYAN),
            *[Dot(point, color=ACCENT_MINT, radius=0.085)
              for point in (LEFT * 0.45, UP * 0.35, RIGHT * 0.55 + DOWN * 0.25)],
        )
        graph = VGroup(graph_shape, label("grafo", 23, TEXT_MAIN).next_to(graph_shape, DOWN, buff=0.25))
        graph.scale(1.15).move_to(RIGHT * 3.3 + DOWN * 0.1)
        table = VGroup(*[Square(side_length=0.42, color=ACCENT_INDIGO, stroke_width=1.8)
                         for _ in range(6)]).arrange_in_grid(rows=2, cols=3, buff=0.05)
        table.add(label("frecuencias", 23, TEXT_MAIN).next_to(table, DOWN, buff=0.22))
        table.move_to(RIGHT * 3.3 + DOWN * 0.1)
        geometry = VGroup(Polygon(LEFT * 0.55 + DOWN * 0.3, RIGHT * 0.55 + DOWN * 0.3,
                                  UP * 0.55, color=ACCENT_VINO),
                          Dot(UP * 0.55, color=ACCENT_TERRACOTTA),
                          label("geometría", 23, TEXT_MAIN)).arrange(DOWN, buff=0.18)
        geometry.move_to(RIGHT * 3.3 + DOWN * 0.1)
        self.play(FadeIn(graph), run_time=0.7)
        self.wait(1.0)
        self.play(Transform(graph, table), run_time=1.0)
        self.wait(1.0)
        self.play(Transform(graph, geometry), run_time=1.0)
        self.wait(1.5)


# class MenuTecnicas(BaseScene):
#     def construct(self):
#         self.play(Write(self.title("El enunciado no marca la técnica")))
#         names = ["Programación dinámica", "Árboles de sufijos", "Teoría de grafos",
#                  "Matemáticas avanzadas", "Flujos máximos", "Recorrido de Euler"]
#         colors = [ACCENT_CYAN, ACCENT_INDIGO, ACCENT_MINT, ACCENT_TERRACOTTA, ACCENT_VINO, TEXT_MUTED]
#         tiles = VGroup(*[card(name, 3.6, 0.92, color, 21) for name, color in zip(names, colors)])
#         tiles.arrange_in_grid(rows=3, cols=2, buff=(0.3, 0.26)).move_to(LEFT * 1.75 + DOWN * 0.05)
#         clock = Circle(radius=0.7, color=ACCENT_TERRACOTTA, stroke_width=2.6).move_to(RIGHT * 4.55 + UP * 0.2)
#         hand1 = Line(clock.get_center(), clock.get_center() + UP * 0.45, color=TEXT_MAIN, stroke_width=2.0)
#         hand2 = Line(clock.get_center(), clock.get_center() + RIGHT * 0.32, color=TEXT_MAIN, stroke_width=2.0)
#         clock_group = VGroup(clock, hand1, hand2)
#         unknown = MathTex(r"?", color=ACCENT_TERRACOTTA, font_size=40).next_to(clock, DOWN, buff=0.4)
#         self.play(LaggedStart(*[FadeIn(tile) for tile in tiles], lag_ratio=0.12), run_time=2.0)
#         self.wait(0.8)
#         self.play(Create(clock_group), FadeIn(unknown), run_time=0.8)
#         for tile in (tiles[0], tiles[2], tiles[4], tiles[1]):
#             self.play(Indicate(tile, color=ACCENT_CYAN), run_time=0.75)
#             self.play(Rotate(hand2, angle=-PI / 5, about_point=clock.get_center()), run_time=0.45)
#         self.wait(1.6)

class MenuTecnicas(BaseScene):
    def construct(self):
        self.play(Write(self.title("El enunciado no marca la técnica")))
        
        # Lista masiva de 28 temas reales de ICPC
        topics = [
            "Two Pointers", "Binary Search", "Segment Tree", "Fenwick Tree",
            "Trie", "Treap", "DSU", "Heavy-Light Decomp.",
            "Centroid Decomp.", "Binary Lifting", "Max Flow (Dinic)", "Min Cost Flow",
            "Tarjan / SCC", "2-SAT", "FFT / NTT", "Matrix Expo",
            "Modular Inverse", "Sieve / Primes", "Convex Hull Trick", "Li Chao Tree",
            "Suffix Array", "KMP / Z-Algo", "DP Optimization", "Digit DP",
            "State Compression", "Meet-in-the-Middle", "Randomized", "GNU PBDS"
        ]
        
        # Paleta variada para simular la diversidad y caos del menú
        color_pool = [ACCENT_CYAN, ACCENT_INDIGO, ACCENT_MINT, ACCENT_TERRACOTTA, ACCENT_VINO, TEXT_MUTED]
        
        # Tarjetas compactas en rejilla de 4 columnas x 7 filas
        tiles = VGroup(*[
            card(name, 2.1, 0.45, color_pool[i % len(color_pool)], 11) 
            for i, name in enumerate(topics)
        ])
        tiles.arrange_in_grid(rows=7, cols=4, buff=(0.14, 0.1)).move_to(LEFT * 1.8 + DOWN * 0.05)
        
        # Reloj y temporizador en la derecha
        clock = Circle(radius=0.7, color=ACCENT_TERRACOTTA, stroke_width=2.6).move_to(RIGHT * 4.55 + UP * 0.2)
        hand1 = Line(clock.get_center(), clock.get_center() + UP * 0.45, color=TEXT_MAIN, stroke_width=2.0)
        hand2 = Line(clock.get_center(), clock.get_center() + RIGHT * 0.32, color=TEXT_MAIN, stroke_width=2.0)
        clock_group = VGroup(clock, hand1, hand2)
        unknown = MathTex(r"?", color=ACCENT_TERRACOTTA, font_size=40).next_to(clock, DOWN, buff=0.4)
        
        # 1. Aparición masiva del menú completo
        self.play(LaggedStart(*[FadeIn(tile, scale=0.9) for tile in tiles], lag_ratio=0.02), run_time=1.8)
        self.wait(0.4)
        
        # 2. Entra el reloj corriendo
        self.play(Create(clock_group), FadeIn(unknown), run_time=0.8)
        
        # 3. Efecto de parpadeo tipo "focos fundidos" en la gran mayoría de técnicas desconocidas
        flicker_indices = [i for i in range(len(topics)) if i not in [1, 2, 4, 10, 16, 20]]
        
        for _ in range(2):
            self.play(
                *[tile.animate.set_opacity(0.2) for i, tile in enumerate(tiles) if i in flicker_indices],
                run_time=0.12
            )
            self.play(
                *[tile.animate.set_opacity(0.9) for i, tile in enumerate(tiles) if i in flicker_indices],
                run_time=0.12
            )
        
        # Quedan opacas/atenuadas simbolizando las que no conoces o descartas
        self.play(
            *[tile.animate.set_opacity(0.22) for i, tile in enumerate(tiles) if i in flicker_indices],
            run_time=0.8
        )
        
        # 4. Exploración de algunas opciones candidatas mientras avanza el reloj
        candidate_indices = [1, 4, 16, 2]
        for idx in candidate_indices:
            self.play(Indicate(tiles[idx], color=ACCENT_CYAN, scale_factor=1.1), run_time=0.6)
            self.play(Rotate(hand2, angle=-PI / 5, about_point=clock.get_center()), run_time=0.4)
        
        self.wait(1.5)

class DistribucionProblemas(BaseScene):
    def construct(self):
        self.play(Write(self.title("Distribución de problemas resueltos")))

        # Tus datos exactos (Problemas [0-10] -> Cantidad de equipos)
        problems = list(range(11))
        teams_count = [4, 5, 5, 9, 18, 8, 9, 6, 11, 1, 2]

        # 1. Configuración de ejes compactos y bien escalados (tope en y=20 para dejar espacio a los corchetes)
        ax = Axes(
            x_range=[-0.5, 10.5, 1],
            y_range=[0, 20, 5],
            x_length=9.5,
            y_length=3.4,
            axis_config={
                "color": TEXT_MUTED, 
                "font_size": 14,
                "stroke_width": 1.5,
            },
        ).move_to(DOWN * 0.5)

        ax.add_coordinates()

        x_label = label("Problemas resueltos", 16, TEXT_MUTED).next_to(ax.x_axis, DOWN, buff=0.25)
        y_label = label("Nro. equipos", 16, TEXT_MUTED).next_to(ax.y_axis, UP, buff=0.1).set_color(TEXT_MUTED)
        
        self.play(Create(ax), FadeIn(x_label), FadeIn(y_label), run_time=0.8)

        # 2. Generación de barras estilizadas ancladas al 0
        bars_group = VGroup()
        for x, y in zip(problems, teams_count):
            if x >= 10:
                col = ACCENT_TERRACOTTA # Pocos (10)
            elif x >= 8:
                col = ACCENT_MINT      # Mejores (8-9)
            elif 2 <= x <= 6:
                col = ACCENT_CYAN      # Mayoría (2-6)
            else:
                col = TEXT_MUTED       # Resto (0-1)
            
            bar = Rectangle(
                width=0.45, 
                height=ax.y_axis.unit_size * y, 
                fill_color=col, 
                fill_opacity=0.65,
                stroke_width=1,
                stroke_color=col
            )
            bar.move_to(ax.c2p(x, 0), aligned_edge=DOWN)
            bars_group.add(bar)

        self.play(LaggedStart(*[FadeIn(b, shift=UP*0.1) for b in bars_group], lag_ratio=0.06), run_time=1.2)
        self.wait(0.6)

        # 3. Tres corchetes colocados ARRIBA indicando los rangos solicitados
        # Mayoría: 2–6 (abarca desde el índice 2 hasta el 6)
        brace_majority = BraceBetweenPoints(
            ax.c2p(1.75, 18), ax.c2p(6.25, 18), direction=UP, color=ACCENT_CYAN
        )
        text_majority = label("mayoría (2–6)", 13, ACCENT_CYAN).next_to(brace_majority, UP, buff=0.1)

        # Mejores: 8–9 (abarca desde el índice 8 hasta el 9)
        brace_elite = BraceBetweenPoints(
            ax.c2p(7.75, 13), ax.c2p(9.25, 13), direction=UP, color=ACCENT_MINT
        )
        text_elite = label("mejores (8–9)", 13, ACCENT_MINT).next_to(brace_elite, UP, buff=0.1)

        # Pocos: 10 (en la barra del índice 10)
        brace_few = BraceBetweenPoints(
            ax.c2p(9.75, 4), ax.c2p(10.25, 4), direction=UP, color=ACCENT_TERRACOTTA
        )
        text_few = label("pocos (10)", 13, ACCENT_TERRACOTTA).next_to(brace_few, UP, buff=0.1)

        self.play(
            GrowFromCenter(brace_majority), FadeIn(text_majority),
            GrowFromCenter(brace_elite), FadeIn(text_elite),
            GrowFromCenter(brace_few), FadeIn(text_few),
            run_time=0.9
        )
        self.wait(2.0)