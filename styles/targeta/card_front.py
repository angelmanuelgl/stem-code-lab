from manim import *

# Tarjeta 90 x 50 mm (formato estándar en México). 1 unidad de manim = 1 cm.
# Render a 1800x1000 px (~500 dpi). Frame 9.0 x 5.0 unidades.
config.pixel_width = 1800
config.pixel_height = 1000
config.frame_width = 9.0
config.frame_height = 5.0

# Margen de seguridad para texto importante: 4 mm desde el borde -> |x|<4.1, |y|<2.1


class CardFront(Scene):
    def construct(self):
        COLOR_BG = "#14121E"
        COLOR_CYAN = "#00E5FF"
        COLOR_TEAL = "#2DD4BF"
        COLOR_BLUE = "#3B82F6"
        COLOR_INDIGO = "#6366F1"
        COLOR_WINE = "#9D174D"
        COLOR_TEXT = "#ECEFF4"
        COLOR_MUTED = "#64748B"

        self.camera.background_color = COLOR_BG

        # Malla de fondo
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 0.5],
            y_range=[-2.5, 2.5, 0.5],
            x_length=9.0, y_length=5.0,
            background_line_style={"stroke_color": COLOR_MUTED, "stroke_width": 0.6, "stroke_opacity": 0.15},
            axis_config={"stroke_opacity": 0},
        )
        self.add(grid)

        # Grafo de nodos en las esquinas
        node_positions = [
            [-4.0, 2.0, 0], [-3.2, 1.55, 0], [-4.0, -1.9, 0], [-3.2, -1.5, 0],
            [4.0, 2.0, 0], [3.2, 1.55, 0], [4.0, -1.9, 0], [3.2, -1.5, 0],
        ]
        graph_group = VGroup()
        for pos in node_positions:
            graph_group.add(Dot(point=pos, color=COLOR_INDIGO, radius=0.05).set_opacity(0.45))
        for i, j in [(0, 1), (2, 3), (4, 5), (6, 7)]:
            graph_group.add(Line(node_positions[i], node_positions[j],
                                 stroke_color=COLOR_WINE, stroke_width=1, stroke_opacity=0.35))
        self.add(graph_group)

        # Fórmulas laterales (decorativas)
        left_specs = [
            (r"O(\log n)", [-3.5, 0.95, 0], COLOR_TEAL, 20),
            (r"dX_t = \mu\,dt + \sigma\,dW_t", [-3.5, 0.2, 0], COLOR_WINE, 14),
            (r"\gamma = \dfrac{1}{\sqrt{1 - v^2/c^2}}", [-3.5, -0.6, 0], COLOR_CYAN, 16),
        ]
        right_specs = [
            (r"A = U\Sigma V^{T}", [3.5, 0.95, 0], COLOR_BLUE, 18),
            (r"\int_X f \, d\mu", [3.5, 0.2, 0], COLOR_TEAL, 20),
            (r"\nabla \times \vec{F}", [3.5, -0.6, 0], COLOR_MUTED, 20),
        ]
        side = VGroup()
        for tex, pos, color, fs in left_specs + right_specs:
            m = MathTex(tex, color=color, font_size=fs).set_opacity(0.8)
            m.move_to(pos)
            side.add(m)
        self.add(side)

        # Bloque central
        halo = Circle(radius=1.55, stroke_color=COLOR_CYAN, stroke_width=1, stroke_opacity=0.25)
        halo.set_fill(COLOR_INDIGO, opacity=0.05)

        title = Tex(r"\textbf{Another Math Channel}", color=COLOR_TEXT, font_size=34)
        accent = Line(LEFT * 1.3, RIGHT * 1.3, stroke_color=COLOR_CYAN, stroke_width=1.5, stroke_opacity=0.6)
        author = Tex(r"\textit{by} \textbf{AngelGL}", color=COLOR_CYAN, font_size=24)
        subtitle = Tex(r"CS \quad $\bullet$ \quad Math \quad $\bullet$ \quad Physics",
                       color=COLOR_TEAL, font_size=20)

        block = VGroup(title, accent, author, subtitle).arrange(DOWN, buff=0.18)
        block.move_to([0, 0.2, 0])
        halo.move_to(block.get_center())
        self.add(halo, block)

        # URL abajo
        url = Text("youtube.com/@Another.Math.Channel", font="monospace",
                   font_size=16, color=COLOR_MUTED)
        url.move_to([0, -1.95, 0])
        self.add(url)
