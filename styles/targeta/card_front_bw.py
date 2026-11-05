from manim import *

# Versión BLANCO Y NEGRO (tinta pura, sin grises) de la tarjeta 90 x 50 mm.
# Los roles de color del banner se traducen a: grosor de línea, línea sólida/punteada,
# puntos rellenos/huecos y un recuadro negro invertido. Nada depende del tono.
config.pixel_width = 1800
config.pixel_height = 1000
config.frame_width = 9.0
config.frame_height = 5.0

INK = "#000000"
PAPER = "#FFFFFF"


def ink_tex(tex, fs):
    return MathTex(tex, color=INK, font_size=fs)


class CardFrontBW(Scene):
    def construct(self):
        self.camera.background_color = PAPER

        # Marco exterior doble (queda dentro de la zona segura de corte)
        frame_outer = RoundedRectangle(width=8.5, height=4.5, corner_radius=0.18,
                                       stroke_color=INK, stroke_width=3, fill_opacity=0)
        frame_inner = RoundedRectangle(width=8.3, height=4.3, corner_radius=0.14,
                                       stroke_color=INK, stroke_width=1.5, fill_opacity=0)
        self.add(frame_outer, frame_inner)

        # Textura: retícula de puntos (en vez de malla gris)
        dots = VGroup()
        for x in np.arange(-3.0, 3.01, 0.5):
            for y in np.arange(-1.5, 1.51, 0.5):
                if abs(x) < 2.4 and abs(y) < 1.7:
                    continue  # deja libre el centro
                dots.add(Dot([x, y, 0], radius=0.012, color=INK))
        self.add(dots)

        # Grafo de esquinas: nodos rellenos / huecos, aristas sólidas / punteadas
        P = [[-3.9, 1.85, 0], [-3.1, 1.45, 0], [-3.9, -1.85, 0], [-3.1, -1.45, 0],
             [3.9, 1.85, 0], [3.1, 1.45, 0], [3.9, -1.85, 0], [3.1, -1.45, 0]]
        graph = VGroup()
        graph.add(Line(P[0], P[1], stroke_color=INK, stroke_width=2.5))
        graph.add(DashedLine(P[2], P[3], stroke_color=INK, stroke_width=2.5, dash_length=0.08))
        graph.add(DashedLine(P[4], P[5], stroke_color=INK, stroke_width=2.5, dash_length=0.08))
        graph.add(Line(P[6], P[7], stroke_color=INK, stroke_width=2.5))
        for i, p in enumerate(P):
            d = Dot(p, radius=0.07, color=INK)
            if i % 2 == 1:
                d.set_fill(PAPER, 1).set_stroke(INK, 2.5)
            graph.add(d)
        self.add(graph)

        # Fórmulas laterales: importancia = tamaño y trazo, no color
        left = [(r"O(\log n)", [-3.3, 0.95, 0], 22),
                (r"dX_t = \mu\,dt + \sigma\,dW_t", [-3.3, 0.2, 0], 15),
                (r"\gamma = \dfrac{1}{\sqrt{1 - v^2/c^2}}", [-3.3, -0.6, 0], 17)]
        right = [(r"A = U\Sigma V^{T}", [3.3, 0.95, 0], 20),
                 (r"\int_X f \, d\mu", [3.3, 0.2, 0], 22),
                 (r"\nabla \times \vec{F}", [3.3, -0.6, 0], 22)]
        for tex, pos, fs in left + right:
            self.add(ink_tex(tex, fs).move_to(pos))

        # Bloque central
        halo = Circle(radius=1.55, stroke_color=INK, stroke_width=2.5)
        halo_dash = DashedVMobject(
            Circle(radius=1.68, stroke_color=INK, stroke_width=2),
            num_dashes=60, dashed_ratio=0.5)

        title = Tex(r"\textbf{Another Math Channel}", color=INK, font_size=34)
        accent = Line(LEFT * 1.3, RIGHT * 1.3, stroke_color=INK, stroke_width=3)
        author = Tex(r"\textit{by} \textbf{AngelGL}", color=INK, font_size=24)
        sub_txt = Tex(r"CS \quad $\bullet$ \quad Math \quad $\bullet$ \quad Physics",
                      color=PAPER, font_size=20)
        sub_box = RoundedRectangle(width=sub_txt.width + 0.4, height=sub_txt.height + 0.25,
                                   corner_radius=0.1, fill_color=INK, fill_opacity=1,
                                   stroke_color=INK, stroke_width=1)
        sub_box.move_to(sub_txt)
        subtitle = VGroup(sub_box, sub_txt)

        block = VGroup(title, accent, author, subtitle).arrange(DOWN, buff=0.17)
        block.move_to([0, 0.15, 0])
        halo.move_to(block.get_center())
        halo_dash.move_to(block.get_center())
        self.add(halo_dash, halo, block)

        # URL
        url = Text("youtube.com/@Another.Math.Channel", font="monospace",
                   font_size=16, color=INK)
        url.move_to([0, -1.9, 0])
        self.add(url)
