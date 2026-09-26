from manim import *
import numpy as np

class EnvironmentTestSuite(Scene):
    def construct(self):
        # 1. Test de LaTeX y Tipografía Vectorial
        title = Tex(r"\textbf{Manim Environment Verification}", font_size=36)
        title.to_edge(UP)
        
        formula = MathTex(
            r"e^{i\pi} + 1 = 0",
            r"\quad \Longleftrightarrow \quad",
            r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}",
            font_size=32
        )
        formula.next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(formula, shift=UP))
        self.wait(0.5)

        # 2. Test de Grafos y Redes (networkx / scipy integration)
        vertices = [1, 2, 3, 4, 5]
        edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4)]
        
        graph = Graph(
            vertices, 
            edges, 
            layout="circular", 
            layout_scale=1.5,
            vertex_config={"radius": 0.15, "color": BLUE},
            edge_config={"stroke_width": 2, "color": GRAY}
        ).to_edge(LEFT, buff=1.0)

        # 3. Test de Funciones Numéricas y Plotting (numpy integration)
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1, 3, 1],
            x_length=4,
            y_length=3,
            axis_config={"include_numbers": False}
        ).to_edge(RIGHT, buff=1.0)

        curve = axes.plot(lambda x: x**2 * np.sin(3 * x), color=RED)
        curve_label = axes.get_graph_label(curve, label=MathTex(r"f(x) = x^2 \sin(3x)", font_size=24))

        # Animación paralela de estructuras
        self.play(
            Create(graph),
            Create(axes),
            run_time=2
        )
        self.play(
            Create(curve),
            Write(curve_label),
            run_time=1.5
        )
        self.wait(1)

        # Limpieza y salida
        self.play(
            *[Uncreate(obj) for obj in [title, formula, graph, axes, curve, curve_label]]
        )
        self.wait(0.5)