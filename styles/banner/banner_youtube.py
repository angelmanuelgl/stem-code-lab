from manim import *

# Configuración de resolución exacta para Banner de YouTube (2048x1152)
config.pixel_width = 2048
config.pixel_height = 1152
config.frame_width = 16.0
config.frame_height = 9.0

# ---------------------------------------------------------------------------
# ZONAS SEGURAS DE YOUTUBE (referencia, en unidades de manim, centradas en 0,0)
#   TV / banner completo:        16.0 x 9.0
#   Visible en computadoras:     16.0 x 3.3   -> y en [-1.65, 1.65]
#   Visible en todos los disp.:   9.65 x 2.64  -> x en [-4.825, 4.825], y en [-1.32, 1.32]
# ---------------------------------------------------------------------------


class YouTubeBanner(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # 1. PALETA DE COLORES
        # ---------------------------------------------------------
        COLOR_BG = "#14121E"
        COLOR_CYAN = "#00E5FF"
        COLOR_TEAL = "#2DD4BF"
        COLOR_BLUE = "#3B82F6"
        COLOR_INDIGO = "#6366F1"
        COLOR_WINE = "#9D174D"
        COLOR_TEXT = "#ECEFF4"
        COLOR_MUTED = "#64748B"

        self.camera.background_color = COLOR_BG

        # ---------------------------------------------------------
        # 2. CAPA DE FONDO: malla + grafo de nodos (esquinas, TV-only)
        # ---------------------------------------------------------
        grid = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-4.5, 4.5, 1],
            background_line_style={"stroke_color": COLOR_MUTED, "stroke_width": 1, "stroke_opacity": 0.15},
            axis_config={"stroke_opacity": 0},
        )
        self.add(grid)

        node_positions = [
            [-6.5, 2.8, 0], [-5.0, 3.5, 0], [-7.0, -3.0, 0], [-5.2, -2.5, 0],
            [6.5, 3.0, 0], [5.2, 2.2, 0], [7.0, -2.8, 0], [5.5, -3.2, 0],
        ]
        graph_group = VGroup()
        for pos in node_positions:
            dot = Dot(point=pos, color=COLOR_INDIGO, radius=0.08)
            dot.set_opacity(0.4)
            graph_group.add(dot)
        for i, j in [(0, 1), (2, 3), (4, 5), (6, 7), (1, 4), (3, 7)]:
            graph_group.add(Line(node_positions[i], node_positions[j],
                                  stroke_color=COLOR_WINE, stroke_width=1, stroke_opacity=0.25))
        self.add(graph_group)

        # ---------------------------------------------------------
        # 3. FRANJA TV-ONLY (|y| > 1.65): textura decorativa con el resto de temas
        # ---------------------------------------------------------
        tv_only_specs = [
            (r"\pi_1(S^1) = \mathbb{Z}", [-6.1, 2.5, 0], COLOR_TEAL),                                    # topología
            (r"\lim_{x \to a} f(x) = L", [-2.0, 3.85, 0], COLOR_MUTED),                                  # límites
            (r"T_pM \cong \mathbb{R}^n", [2.0, 3.85, 0], COLOR_MUTED),                                   # variedades
            (r"k\text{-}NN, \;\; \text{PCA}", [6.1, 2.5, 0], COLOR_BLUE),                                # clasificadores
            (r"\mathcal{C} \subset [0,1],\; |\mathcal{C}| = 2^{\aleph_0}", [-6.1, -2.5, 0], COLOR_WINE),   # Cantor
            (r"(f * g)(t) = \int f(\tau)g(t-\tau)\,d\tau", [-2.0, -3.85, 0], COLOR_INDIGO),               # CNN / convolución
            (r"\nabla I(x, y)", [2.0, -3.85, 0], COLOR_CYAN),                                             # visión computacional
            (r"\int_X f \, d\mu", [6.1, -2.5, 0], COLOR_TEAL),                                            # medida / Lebesgue
            (r"\triangle ABC \cong \triangle DEF", [-4.3, 4.05, 0], COLOR_MUTED),                         # geometría euclidiana
            (r"\kappa = \dfrac{d\theta}{ds}", [4.3, 4.05, 0], COLOR_MUTED),                               # geometría dif. discreta
            (r"A \cup B, \; A \cap B, \; A^{c}", [-4.3, -4.05, 0], COLOR_MUTED),                          # conjuntos
            (r"P_1 \parallel P_2 \parallel \cdots \parallel P_n", [4.3, -4.05, 0], COLOR_MUTED),          # paralelismo
        ]
        tv_only = VGroup()
        for tex, pos, color in tv_only_specs:
            m = MathTex(tex, color=color, font_size=15)
            m.set_opacity(0.4)
            m.move_to(pos)
            tv_only.add(m)
        self.add(tv_only)

        # etiquetas cortas junto a los nodos del grafo (también TV-only)
        for label, pos in [("Segment Tree", [-5.6, -3.05, 0]), ("Lazy Prop.", [5.5, -3.55, 0]),
                            ("String Match.", [-6.9, 2.35, 0]), ("Parallelism", [6.9, 2.55, 0])]:
            t = Text(label, font="monospace", font_size=13, color=COLOR_MUTED)
            t.set_opacity(0.5)
            t.move_to(pos)
            self.add(t)

        # ---------------------------------------------------------
        # 4. COLUMNAS "VISIBLE EN COMPUTADORAS" (desktop-safe, x en [4.825, 8] y [-8, -4.825])
        # ---------------------------------------------------------
        outer_left_specs = [
            (r"\partial_t u + (u\!\cdot\!\nabla)u = -\tfrac{1}{\rho}\nabla p + \nu\nabla^2 u", [-6.35, 1.1, 0], COLOR_TEAL, 13),
            (r"dX_t = \mu\,dt + \sigma\,dW_t", [-6.35, 0, 0], COLOR_WINE, 16),
            (r"\gamma = \dfrac{1}{\sqrt{1 - v^2/c^2}}", [-6.35, -1.1, 0], COLOR_CYAN, 16),
        ]
        outer_right_specs = [
            (r"V(s) = \max_a\big[R(s,a) + \gamma V(s')\big]", [6.35, 1.1, 0], COLOR_INDIGO, 14),
            (r"R^{i}{}_{jkl}", [6.35, 0, 0], COLOR_WINE, 18),
            (r"\nabla \times \vec{F}", [6.35, -1.1, 0], COLOR_MUTED, 18),
        ]
        desktop_safe = VGroup()
        for tex, pos, color, fs in outer_left_specs + outer_right_specs:
            m = MathTex(tex, color=color, font_size=fs)
            m.set_opacity(0.75)
            m.move_to(pos)
            desktop_safe.add(m)
        self.add(desktop_safe)

        # ---------------------------------------------------------
        # 5. COLUMNAS "VISIBLE EN TODOS LOS DISPOSITIVOS" (mobile-safe, x en [-4.825, 4.825])
        # ---------------------------------------------------------
        # Izquierda: complejidad + cálculo + algoritmos
        bigo_tag = MathTex(r"O(\log n)", color=COLOR_TEAL, font_size=18).move_to([-3.7, 1.02, 0])

        axes_mini = Axes(
            x_range=[0, 5, 1], y_range=[-1, 2, 1],
            x_length=1.7, y_length=1.0,
            axis_config={"stroke_color": COLOR_MUTED, "stroke_opacity": 0.35, "include_tip": False},
        ).move_to([-3.7, -0.1, 0])
        curve = axes_mini.plot(lambda x: np.sin(x * 1.5) * np.exp(-x * 0.2), color=COLOR_CYAN, stroke_width=2)
        area = axes_mini.get_area(curve, x_range=[0.5, 4], color=COLOR_WINE, opacity=0.35)
        calculus_mini = VGroup(axes_mini, curve, area)

        algo_tag = MathTex(r"\text{KMP} \cdot \text{DP}", color=COLOR_MUTED, font_size=14).move_to([-3.7, -1.05, 0])

        left_inner = VGroup(bigo_tag, calculus_mini, algo_tag)

        # Derecha: álgebra lineal + geometría + probabilidad
        svd_tag = MathTex(r"A = U\Sigma V^{T}", color=COLOR_BLUE, font_size=17).move_to([3.7, 1.02, 0])

        rotation_matrix = MathTex(
            r"R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}",
            color=COLOR_TEXT, font_size=20,
        ).move_to([3.7, -0.05, 0])

        gauss_tag = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2}dx = \sqrt{\pi}", color=COLOR_TEAL, font_size=14).move_to([3.7, -1.05, 0])

        right_inner = VGroup(svd_tag, rotation_matrix, gauss_tag)

        mobile_safe = VGroup(left_inner, right_inner)
        self.add(mobile_safe)

        # ---------------------------------------------------------
        # 6. ZONA SEGURA CENTRAL: título, autor, temas
        # ---------------------------------------------------------
        halo = Circle(radius=2.05, stroke_color=COLOR_CYAN, stroke_width=1, stroke_opacity=0.25)
        halo.set_fill(COLOR_INDIGO, opacity=0.05)

        channel_title = Tex(r"\textbf{Another Math Channel}", color=COLOR_TEXT, font_size=38)
        author_line = Tex(r"\textit{by} \textbf{AngelGL}", color=COLOR_CYAN, font_size=24)
        subtitle_line = Tex(r"CS \quad $\bullet$ \quad Math \quad $\bullet$ \quad Physics", color=COLOR_TEAL, font_size=20)
        accent_line = Line(LEFT * 1.5, RIGHT * 1.5, stroke_color=COLOR_CYAN, stroke_width=1.5, stroke_opacity=0.6)

        text_block = VGroup(channel_title, accent_line, author_line, subtitle_line).arrange(DOWN, buff=0.2)
        text_block.move_to(ORIGIN)
        halo.move_to(text_block.get_center())

        self.add(VGroup(halo, text_block))

        # ---------------------------------------------------------
        # 7. GUÍAS OPCIONALES DE PRUEBA (Descomentar para depurar)
        # ---------------------------------------------------------
        # safe_box_mobile = Rectangle(width=9.65, height=2.64, color=RED, stroke_width=1)
        # safe_box_desktop = Rectangle(width=16.0, height=3.3, color=YELLOW, stroke_width=1)
        # self.add(safe_box_mobile, safe_box_desktop)