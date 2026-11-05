from manim import *
from ..paper_theme import *

# Banner YouTube 2048x1152 -> frame 16 x 9
config.pixel_width = 2048
config.pixel_height = 1152
config.frame_width = 16.0
config.frame_height = 9.0

# ZONAS SEGURAS (centradas en 0,0)
#   TV completo:                 16.0 x 9.0
#   Computadoras:                16.0 x 3.3   -> |y| <= 1.65
#   Todos los dispositivos:       9.65 x 2.64 -> |x| <= 4.825, |y| <= 1.32
#
# Render:  manim -s banner_paper.py YouTubeBannerPaper
# Para depurar: cambia DEBUG = True


DEBUG = False


class YouTubeBannerPaper(PaperScene):
    def construct(self):
        # --------------------------------------------------------------
        # 1. FONDO: papel milimetrado muy tenue
        # --------------------------------------------------------------
        grid = NumberPlane(
            x_range=[-8, 8, 1], y_range=[-4.5, 4.5, 1],
            background_line_style={"stroke_color": RULE, "stroke_width": SW.GRID, "stroke_opacity": 0.7},
            faded_line_ratio=1,
            axis_config={"stroke_opacity": 0},
        )
        self.add(grid)

        # --------------------------------------------------------------
        # 2. GRAFO EN LAS ESQUINAS (solo TV): nodos rellenos/huecos, aristas sólidas/punteadas
        # --------------------------------------------------------------
        P = [[-6.5, 2.8, 0], [-5.0, 3.5, 0], [-7.0, -3.0, 0], [-5.2, -2.5, 0],
             [6.5, 3.0, 0], [5.2, 2.2, 0], [7.0, -2.8, 0], [5.5, -3.2, 0]]
        dashed = {(2, 3), (1, 4), (3, 7)}
        graph = VGroup()
        for i, j in [(0, 1), (2, 3), (4, 5), (6, 7), (1, 4), (3, 7)]:
            graph.add(edge(P[i], P[j], dashed=(i, j) in dashed, stroke=SW.AUX, color=GRAPHITE))
        for i, p in enumerate(P):
            d = Dot(p, radius=0.08, color=GRAPHITE)
            if i % 2 == 1:  # hueco = variable / incógnita
                d.set_fill(PAPER, 1).set_stroke(GRAPHITE, SW.AUX)
            graph.add(d)
        self.add(graph)

        # etiquetas junto a los nodos (TV-only)
        for label, pos in [("Segment Tree", [-5.2, -2.85, 0]), ("Lazy Prop.", [5.5, -3.55, 0]),
                           ("String Match.", [-6.5, 2.45, 0]), ("Parallelism", [6.5, 2.65, 0])]:
            self.add(Tex(r"\texttt{" + label + "}", font_size=FS.MICRO - 6, color=GRAPHITE).move_to(pos))

        # --------------------------------------------------------------
        # 3. FRANJA TV-ONLY (|y| > 1.65): temas del canal en tinta de contexto
        # --------------------------------------------------------------
        tv_specs = [
            (r"\pi_1(S^1) = \mathbb{Z}", [-6.0, 2.0, 0]),
            (r"\lim_{x \to a} f(x) = L", [-2.0, 3.85, 0]),
            (r"T_pM \cong \mathbb{R}^n", [2.0, 3.85, 0]),
            (r"k\text{-}NN, \;\; \text{PCA}", [6.0, 1.9, 0]),
            (r"\mathcal{C} \subset [0,1],\; |\mathcal{C}| = 2^{\aleph_0}", [-6.0, -2.0, 0]),
            (r"(f * g)(t) = \int f(\tau)g(t-\tau)\,d\tau", [-2.0, -3.85, 0]),
            (r"\nabla I(x, y)", [2.0, -3.85, 0]),
            (r"\int_X f \, d\mu", [6.0, -1.95, 0]),
            (r"\triangle ABC \cong \triangle DEF", [-4.6, 4.1, 0]),
            (r"\kappa = \dfrac{d\theta}{ds}", [4.6, 4.1, 0]),
            (r"A \cup B, \; A \cap B, \; A^{c}", [-4.6, -4.1, 0]),
            (r"P_1 \parallel P_2 \parallel \cdots \parallel P_n", [4.6, -4.1, 0]),
        ]
        for s, pos in tv_specs:
            self.add(tex(s, size=16, color=GRAPHITE).set_opacity(0.8).move_to(pos))

        # --------------------------------------------------------------
        # 4. COLUMNAS "VISIBLE EN COMPUTADORAS" (|x| entre 4.8 y 8, |y| <= 1.65)
        # --------------------------------------------------------------
        outer = [
            (r"\partial_t u + (u\!\cdot\!\nabla)u = -\nabla p + \nu\nabla^2 u", [-6.3, 1.1, 0], INK_SOFT, 13),
            (r"dX_t = \mu\,dt + \sigma\,dW_t", [-6.3, 0, 0], INK, 17),
            (r"\gamma = \dfrac{1}{\sqrt{1 - v^2/c^2}}", [-6.3, -1.1, 0], INK_SOFT, 17),
            (r"V(s) = \max_a\big[R(s,a) + \gamma V(s')\big]", [6.3, 1.1, 0], INK_SOFT, 14),
            (r"R^{i}{}_{jkl}", [6.3, 0, 0], INK, 22),
            (r"\nabla \times \vec{F}", [6.3, -1.1, 0], INK_SOFT, 20),
        ]
        for s, pos, col, fs in outer:
            self.add(tex(s, size=fs, color=col).move_to(pos))

        # --------------------------------------------------------------
        # 5. COLUMNAS "VISIBLE EN TODOS LOS DISPOSITIVOS" (|x| <= 4.825)
        # --------------------------------------------------------------
        # Izquierda: complejidad + cálculo + algoritmos
        bigo = tex(r"O(\log n)", size=20, color=INK).move_to([-3.85, 1.0, 0])

        axes = pen_axes([0, 5, 1], [-1, 2, 1], 1.6, 1.0).move_to([-3.85, -0.1, 0])
        curve = axes.plot(lambda x: np.sin(x * 1.5) * np.exp(-x * 0.2), color=INK, stroke_width=SW.CURVE)
        area = axes.get_area(curve, x_range=[0.5, 4], color=ACCENT, opacity=0.18)  # ← acento de la escena
        calc = VGroup(axes, area, curve)

        algo = tex(r"\text{KMP} \cdot \text{DP}", size=16, color=INK_SOFT).move_to([-3.85, -1.05, 0])

        # Derecha: álgebra lineal + geometría + probabilidad
        svd = tex(r"A = U\Sigma V^{T}", size=18, color=INK).move_to([3.85, 1.0, 0])
        rot = tex(r"R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}",
                  size=16, color=INK).move_to([3.85, -0.05, 0])
        gauss = tex(r"\int_{-\infty}^{\infty} e^{-x^2}dx = \sqrt{\pi}", size=15, color=INK_SOFT).move_to([3.85, -1.05, 0])

        self.add(bigo, calc, algo, svd, rot, gauss)

        # --------------------------------------------------------------
        # 6. ZONA SEGURA CENTRAL: cartucho editorial con título
        # --------------------------------------------------------------
        title = Tex(r"\textbf{Another Math Channel}", color=INK, font_size=38)
        rule = Line(LEFT * 1.6, RIGHT * 1.6, stroke_color=ACCENT, stroke_width=SW.ACCENT)
        author = Tex(r"\textit{by} \textbf{AngelGL}", color=INK, font_size=24)

        sub_txt = Tex(r"CS \quad $\bullet$ \quad Math \quad $\bullet$ \quad Physics", color=PAPER, font_size=20)
        sub_box = RoundedRectangle(width=sub_txt.width + 0.45, height=sub_txt.height + 0.28,
                                   corner_radius=0.1, fill_color=INK, fill_opacity=1,
                                   stroke_color=INK, stroke_width=1).move_to(sub_txt)
        subtitle = VGroup(sub_box, sub_txt)

        block = VGroup(title, rule, author, subtitle).arrange(DOWN, buff=0.17).move_to(ORIGIN)

        # Marco doble (eco del marco de la tarjeta); fondo de papel para limpiar la cuadrícula detrás
        plate_out = RoundedRectangle(width=5.2, height=2.3, corner_radius=0.14,
                                     stroke_color=INK, stroke_width=SW.FRAME,
                                     fill_color=PAPER, fill_opacity=1)
        plate_in = RoundedRectangle(width=5.08, height=2.18, corner_radius=0.11,
                                    stroke_color=INK_SOFT, stroke_width=SW.HAIR, fill_opacity=0)
        self.add(plate_out, plate_in, block)

        # --------------------------------------------------------------
        # 7. GUÍAS DE PRUEBA
        # --------------------------------------------------------------
        if DEBUG:
            self.add(Rectangle(width=9.65, height=2.64, color=RED, stroke_width=1),
                     Rectangle(width=16.0, height=3.3, color=YELLOW, stroke_width=1))
