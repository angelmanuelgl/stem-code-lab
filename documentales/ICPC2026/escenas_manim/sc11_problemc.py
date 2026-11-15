"""Bloque 2: enunciado completo y conteo riguroso de rutas en Clumsy Courier."""
from manim import *
from base_theme import BaseScene, label, formula, grid_graph, card
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


def tex_line(parts, font_size=18, max_width=11.2):
    """Construye una línea/párrafo en LaTeX a partir de tuplas (texto_latex, color)."""
    items = VGroup(*[
        Tex(text, font_size=font_size, color=col)
        for text, col in parts
    ])
    items.arrange(RIGHT, buff=0.06, aligned_edge=DOWN)
    if items.width > max_width:
        items.scale_to_fit_width(max_width)
    return items


def sample_card(title_in, val_in, title_out, val_out, width=11.2):
    """Construye una fila tipo tabla de Sample Input / Output en LaTeX."""
    left_box = RoundedRectangle(
        width=width * 0.485,
        height=0.82,
        corner_radius=0.08,
        stroke_color=TEXT_MUTED,
        stroke_width=1.2,
        fill_color=BG_COLOR,
        fill_opacity=0.85,
    )
    right_box = RoundedRectangle(
        width=width * 0.485,
        height=0.82,
        corner_radius=0.08,
        stroke_color=TEXT_MUTED,
        stroke_width=1.2,
        fill_color=BG_COLOR,
        fill_opacity=0.85,
    )
    row = VGroup(left_box, right_box).arrange(RIGHT, buff=0.18)

    in_hdr = Tex(title_in, font_size=15, color=ACCENT_CYAN)
    in_val = Tex(val_in, font_size=17, color=TEXT_MAIN)
    in_col = VGroup(in_hdr, in_val).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
    in_col.move_to(left_box.get_left() + RIGHT * 0.22, aligned_edge=LEFT)

    out_hdr = Tex(title_out, font_size=15, color=ACCENT_MINT)
    out_val = Tex(val_out, font_size=17, color=ACCENT_TERRACOTTA)
    out_col = VGroup(out_hdr, out_val).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
    out_col.move_to(right_box.get_left() + RIGHT * 0.22, aligned_edge=LEFT)

    return VGroup(row, in_col, out_col)


class EnunciadoCourier(BaseScene):
    def construct(self):
        # 1. Hoja amplia sin título externo superior
        sheet_width = 12.4
        sheet_height = 7.0
        sheet_center = ORIGIN
        sheet_fill = "#1E2430"

        sheet_frame = RoundedRectangle(
            width=sheet_width,
            height=sheet_height,
            corner_radius=0.14,
            stroke_color=ACCENT_INDIGO,
            stroke_width=1.8,
            fill_color=sheet_fill,
            fill_opacity=1.0,
        ).move_to(sheet_center)

        sheet_tag = Tex(
            r"\textbf{Problem C - Clumsy Courier}",
            font_size=25,
            color=ACCENT_CYAN,
        )
        sheet_divider = Line(
            LEFT * (sheet_width / 2 - 0.35),
            RIGHT * (sheet_width / 2 - 0.35),
            color=TEXT_MUTED,
            stroke_width=1.2,
        )
        sheet_header = VGroup(sheet_tag, sheet_divider).arrange(DOWN, buff=0.12)
        sheet_header.move_to(sheet_frame.get_top() + DOWN * 0.44)

        top_limit = sheet_header.get_bottom()[1] - 0.16
        bottom_limit = sheet_frame.get_bottom()[1] + 0.24

        # 2. Enunciado completo en LaTeX con partes clave, límites y restricciones en color
        paragraphs = [
            tex_line([
                (r"A courier must deliver a package across a city. The city's streets form a rectangular", TEXT_MAIN),
            ]),
            tex_line([
                (r"grid with ", TEXT_MAIN),
                (r"$R$", ACCENT_CYAN),
                (r" horizontal streets and ", TEXT_MAIN),
                (r"$C$", ACCENT_CYAN),
                (r" vertical streets. On the city map, the horizontal", TEXT_MAIN),
            ]),
            tex_line([
                (r"streets are numbered from ", TEXT_MAIN),
                (r"$1$", ACCENT_INDIGO),
                (r" to ", TEXT_MAIN),
                (r"$R$", ACCENT_INDIGO),
                (r" from top to bottom, and the vertical streets from ", TEXT_MAIN),
                (r"$1$", ACCENT_INDIGO),
                (r" to ", TEXT_MAIN),
                (r"$C$", ACCENT_INDIGO),
            ]),
            tex_line([
                (r"from left to right. Intersection ", TEXT_MAIN),
                (r"$(r, c)$", ACCENT_MINT),
                (r" is where horizontal street ", TEXT_MAIN),
                (r"$r$", ACCENT_CYAN),
                (r" meets vertical street ", TEXT_MAIN),
                (r"$c$", ACCENT_CYAN),
                (r".", TEXT_MAIN),
            ]),
            tex_line([
                (r"The courier starts at ", TEXT_MAIN),
                (r"$(1, 1)$", ACCENT_MINT),
                (r" and must deliver the package at ", TEXT_MAIN),
                (r"$(R, C)$", ACCENT_MINT),
                (r".", TEXT_MAIN),
            ]),
            tex_line([
                (r"In one move, the courier can follow a street from ", TEXT_MAIN),
                (r"$(r, c)$", ACCENT_CYAN),
                (r" to an adjacent intersection:", TEXT_MAIN),
            ]),
            tex_line([
                (r"$\bullet$ Down, to ", TEXT_MUTED),
                (r"$(r + 1, c)$", ACCENT_INDIGO),
                (r";", TEXT_MUTED),
            ], font_size=17),
            tex_line([
                (r"$\bullet$ Up, to ", TEXT_MUTED),
                (r"$(r - 1, c)$", ACCENT_INDIGO),
                (r";", TEXT_MUTED),
            ], font_size=17),
            tex_line([
                (r"$\bullet$ Right, to ", TEXT_MUTED),
                (r"$(r, c + 1)$", ACCENT_INDIGO),
                (r"; or", TEXT_MUTED),
            ], font_size=17),
            tex_line([
                (r"$\bullet$ Left, to ", TEXT_MUTED),
                (r"$(r, c - 1)$", ACCENT_INDIGO),
                (r".", TEXT_MUTED),
            ], font_size=17),
            tex_line([
                (r"The courier may only travel between intersections in this grid.", TEXT_MAIN),
            ]),
            tex_line([
                (r"The courier is in no hurry to finish the delivery. To make the trip last longer, they want", TEXT_MAIN),
            ]),
            tex_line([
                (r"to choose a route that includes ", TEXT_MAIN),
                (r"exactly $U$ Up", ACCENT_TERRACOTTA),
                (r" moves and ", TEXT_MAIN),
                (r"exactly $L$ Left", ACCENT_TERRACOTTA),
                (r" moves.", TEXT_MAIN),
            ]),
            tex_line([
                (r"The courier is willing to visit any intersection ", TEXT_MAIN),
                (r"more than once", ACCENT_MINT),
                (r", including the starting", TEXT_MAIN),
            ]),
            tex_line([
                (r"and ending intersections.", TEXT_MAIN),
            ]),
            tex_line([
                (r"Count the number of different routes from ", TEXT_MAIN),
                (r"$(1, 1)$", ACCENT_MINT),
                (r" to ", TEXT_MAIN),
                (r"$(R, C)$", ACCENT_MINT),
                (r" that stay within the grid and", TEXT_MAIN),
            ]),
            tex_line([
                (r"contain ", TEXT_MAIN),
                (r"exactly $U$ Up", ACCENT_TERRACOTTA),
                (r" moves and ", TEXT_MAIN),
                (r"exactly $L$ Left", ACCENT_TERRACOTTA),
                (r" moves. Two routes are considered different if", TEXT_MAIN),
            ]),
            tex_line([
                (r"their sequences of moves are different.", TEXT_MAIN),
            ]),
            tex_line([
                (r"\textbf{Input}", ACCENT_CYAN),
            ], font_size=20),
            tex_line([
                (r"The input consists of a single line that contains four integers ", TEXT_MAIN),
                (r"$R, C, U$", ACCENT_CYAN),
                (r" and ", TEXT_MAIN),
                (r"$L$", ACCENT_CYAN),
                (r" (", TEXT_MAIN),
                (r"$2 \le R, C \le 2000$", ACCENT_TERRACOTTA),
            ]),
            tex_line([
                (r"and ", TEXT_MAIN),
                (r"$0 \le U, L \le 2000$", ACCENT_TERRACOTTA),
                (r"), indicating respectively the number of horizontal streets, the number of", TEXT_MAIN),
            ]),
            tex_line([
                (r"vertical streets, the required number of Up moves, and the required number of Left moves.", TEXT_MAIN),
            ]),
            tex_line([
                (r"\textbf{Output}", ACCENT_CYAN),
            ], font_size=20),
            tex_line([
                (r"Output a single line with an integer indicating the number of valid routes. Since this number", TEXT_MAIN),
            ]),
            tex_line([
                (r"can be large, output the remainder of dividing it by ", TEXT_MAIN),
                (r"$998\,244\,353$", ACCENT_MINT),
                (r".", TEXT_MAIN),
            ]),
            sample_card(r"\textbf{Sample input 1}", r"\texttt{2 2 1 0}", r"\textbf{Sample output 1}", r"\texttt{4}"),
            tex_line([
                (r"\textbf{Explanation of sample 1:}", ACCENT_INDIGO),
            ], font_size=18),
            tex_line([
                (r"Each route uses two Down moves, one Up move, and one Right move. Writing directions by", TEXT_MAIN),
            ]),
            tex_line([
                (r"their first letters, the four routes are ", TEXT_MAIN),
                (r"\texttt{DUDR}", ACCENT_MINT),
                (r", ", TEXT_MAIN),
                (r"\texttt{DURD}", ACCENT_MINT),
                (r", ", TEXT_MAIN),
                (r"\texttt{DRUD}", ACCENT_MINT),
                (r", and ", TEXT_MAIN),
                (r"\texttt{RDUD}", ACCENT_MINT),
                (r".", TEXT_MAIN),
            ]),
            tex_line([
                (r"The first two routes visit the starting intersection twice, while the last two routes visit the", TEXT_MAIN),
            ]),
            tex_line([
                (r"destination twice.", TEXT_MAIN),
            ]),
            sample_card(r"\textbf{Sample input 2}", r"\texttt{3 3 1 1}", r"\textbf{Sample output 2}", r"\texttt{280}"),
            sample_card(r"\textbf{Sample input 3}", r"\texttt{2 163 2 0}", r"\textbf{Sample output 3}", r"\texttt{20719340}"),
        ]

        content_group = VGroup(*paragraphs).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        content_group.move_to([sheet_center[0], top_limit, 0], aligned_edge=UP)

        def sync_bounds(group):
            for item in group:
                if item.get_top()[1] > top_limit + 0.02 or item.get_bottom()[1] < bottom_limit - 0.02:
                    item.set_opacity(0.0)
                else:
                    item.set_opacity(1.0)

        sync_bounds(content_group)

        # Máscaras estrictas dentro del recuadro para que nada se salga de los bordes
        top_mask = Rectangle(
            width=sheet_width - 0.08,
            height=max(0.05, sheet_frame.get_top()[1] - top_limit),
            fill_color=sheet_fill,
            fill_opacity=1.0,
            stroke_width=0,
        ).move_to([sheet_center[0], (sheet_frame.get_top()[1] + top_limit) / 2, 0], aligned_edge=ORIGIN)

        bottom_mask = Rectangle(
            width=sheet_width - 0.08,
            height=max(0.05, bottom_limit - sheet_frame.get_bottom()[1]),
            fill_color=sheet_fill,
            fill_opacity=1.0,
            stroke_width=0,
        ).move_to([sheet_center[0], (bottom_limit + sheet_frame.get_bottom()[1]) / 2, 0], aligned_edge=ORIGIN)

        border_overlay = RoundedRectangle(
            width=sheet_width,
            height=sheet_height,
            corner_radius=0.14,
            stroke_color=ACCENT_INDIGO,
            stroke_width=1.8,
            fill_opacity=0.0,
        ).move_to(sheet_center)

        self.play(
            FadeIn(sheet_frame),
            FadeIn(content_group),
            FadeIn(top_mask),
            FadeIn(bottom_mask),
            FadeIn(sheet_header),
            Create(border_overlay),
            run_time=0.9,
        )
        self.wait(0.8)

        # 3. Scroll suave dentro del recuadro
        visible_height = top_limit - bottom_limit
        scroll_distance = max(0.0, content_group.height - visible_height + 0.25)
        start_center = content_group.get_center().copy()

        def update_scroll(mob, alpha):
            dy = interpolate(0.0, scroll_distance, alpha)
            mob.move_to(start_center + UP * dy)
            sync_bounds(mob)

        self.play(
            UpdateFromAlphaFunc(content_group, update_scroll),
            run_time=16.0,
            rate_func=linear,
        )

        # 4. Espera de 3s al final y sello "Próximo video" encima
        self.wait(3.0)

        stamp_box = RoundedRectangle(
            width=4.2,
            height=1.05,
            corner_radius=0.16,
            stroke_color=ACCENT_TERRACOTTA,
            stroke_width=2.6,
            fill_color=BG_COLOR,
            fill_opacity=0.98,
        )
        stamp_text = Tex(
            r"\textbf{Pr\'{o}ximo video}",
            font_size=30,
            color=ACCENT_MINT,
        )
        stamp = VGroup(stamp_box, stamp_text.move_to(stamp_box)).move_to(ORIGIN)

        self.play(FadeIn(stamp, scale=0.92), run_time=0.7)

        # 5. Tras 2 segundos, animación de deshacer para dejar solo el fondo
        self.wait(2.0)

        self.play(
            FadeOut(stamp, scale=0.9),
            FadeOut(content_group, shift=DOWN * 0.15),
            FadeOut(sheet_header, shift=UP * 0.1),
            FadeOut(top_mask),
            FadeOut(bottom_mask),
            Uncreate(border_overlay),
            FadeOut(sheet_frame),
            run_time=1.1,
        )
        self.wait(0.3)



"""Bloque 2B: intuicion visual y ejemplos pequenos de Clumsy Courier."""
from manim import *
from base_theme import BaseScene, label, formula
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


def build_grid_nodes(rows: int, cols: int, cell_size: float = 0.85):
    """Construye líneas de cuadrícula (rows x cols celdas) y diccionario (r, c) -> punto."""
    width = cols * cell_size
    height = rows * cell_size
    origin_shift = LEFT * (width / 2) + UP * (height / 2)

    points = {}
    for r in range(rows):
        for c in range(cols):
            points[(r + 1, c + 1)] = origin_shift + RIGHT * (c * cell_size) + DOWN * (r * cell_size)

    lines = VGroup()
    for r in range(rows):
        p_start = points[(r + 1, 1)]
        p_end = points[(r + 1, cols)]
        lines.add(Line(p_start, p_end, stroke_color=TEXT_MUTED, stroke_width=1.8, stroke_opacity=0.55))

    for c in range(cols):
        p_start = points[(1, c + 1)]
        p_end = points[(rows, c + 1)]
        lines.add(Line(p_start, p_end, stroke_color=TEXT_MUTED, stroke_width=1.8, stroke_opacity=0.55))

    dots = VGroup(*[
        Dot(pt, radius=0.045, color=TEXT_MUTED)
        for pt in points.values()
    ])
    return VGroup(lines, dots), points


def build_path_from_moves(points: dict, start: tuple, moves: list, color):
    """Genera un VMobject de segmentos para una secuencia de movimientos ['R','D','U','L']."""
    curr = start
    segments = VGroup()
    for mv in moves:
        r, c = curr
        if mv == "R":
            nxt = (r, c + 1)
        elif mv == "L":
            nxt = (r, c - 1)
        elif mv == "D":
            nxt = (r + 1, c)
        elif mv == "U":
            nxt = (r - 1, c)
        else:
            raise ValueError(f"Movimiento invalido: {mv}")

        seg = Line(
            points[curr],
            points[nxt],
            stroke_color=color,
            stroke_width=4.2,
        )
        segments.add(seg)
        curr = nxt
    return segments


def build_mini_grid_with_path(rows: int, cols: int, moves: list, color, cell_size: float = 0.34):
    """Crea una copia compacta de la cuadrícula con un camino ya trazado."""
    grid_mob, pts = build_grid_nodes(rows, cols, cell_size=cell_size)
    path_mob = build_path_from_moves(pts, (1, 1), moves, color)
    for seg in path_mob:
        seg.set_stroke(width=2.6)
    start_dot = Dot(pts[(1, 1)], radius=0.035, color=ACCENT_MINT)
    end_dot = Dot(pts[(rows, cols)], radius=0.035, color=ACCENT_TERRACOTTA)
    return VGroup(grid_mob, path_mob, start_dot, end_dot)

"""Bloque 2B: intuicion visual y ejemplos pequenos de Clumsy Courier."""
from manim import *
from base_theme import BaseScene, label, formula
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


def build_grid_nodes(rows: int, cols: int, cell_size: float = 0.85):
    """Construye líneas de cuadrícula (rows x cols celdas) y diccionario (r, c) -> punto."""
    width = (cols - 1) * cell_size
    height = (rows - 1) * cell_size
    origin_shift = LEFT * (width / 2) + UP * (height / 2)

    points = {}
    for r in range(rows):
        for c in range(cols):
            points[(r + 1, c + 1)] = origin_shift + RIGHT * (c * cell_size) + DOWN * (r * cell_size)

    lines = VGroup()
    for r in range(rows):
        p_start = points[(r + 1, 1)]
        p_end = points[(r + 1, cols)]
        lines.add(Line(p_start, p_end, stroke_color=TEXT_MUTED, stroke_width=1.8, stroke_opacity=0.55))

    for c in range(cols):
        p_start = points[(1, c + 1)]
        p_end = points[(rows, c + 1)]
        lines.add(Line(p_start, p_end, stroke_color=TEXT_MUTED, stroke_width=1.8, stroke_opacity=0.55))

    dots = VGroup(*[
        Dot(pt, radius=0.045, color=TEXT_MUTED)
        for pt in points.values()
    ])
    return VGroup(lines, dots), points


def build_path_from_moves(points: dict, start: tuple, moves: list, color):
    """Genera un VMobject de segmentos para una secuencia de movimientos ['R','D','U','L']."""
    curr = start
    segments = VGroup()
    for mv in moves:
        r, c = curr
        if mv == "R":
            nxt = (r, c + 1)
        elif mv == "L":
            nxt = (r, c - 1)
        elif mv == "D":
            nxt = (r + 1, c)
        elif mv == "U":
            nxt = (r - 1, c)
        else:
            raise ValueError(f"Movimiento invalido: {mv}")

        seg = Line(
            points[curr],
            points[nxt],
            stroke_color=color,
            stroke_width=4.2,
        )
        segments.add(seg)
        curr = nxt
    return segments

"""Bloque 2B: intuicion visual y conteo de caminos validos en Clumsy Courier."""
from manim import *
from base_theme import BaseScene, label, formula
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


MOVE_DELTAS = {
    "R": (0, 1),
    "L": (0, -1),
    "D": (1, 0),
    "U": (-1, 0),
}


def validate_path(rows: int, cols: int, start: tuple, goal: tuple, moves: list, exp_u: int, exp_l: int):
    """Verifica que el camino permanezca en [1..rows]x[1..cols], llegue a goal y cumpla U, L."""
    r, c = start
    u_cnt = 0
    l_cnt = 0
    coords = [start]
    for mv in moves:
        dr, dc = MOVE_DELTAS[mv]
        r += dr
        c += dc
        if not (1 <= r <= rows and 1 <= c <= cols):
            raise ValueError(f"Movimiento {mv} se sale de ({rows}x{cols}) en {(r, c)}")
        if mv == "U":
            u_cnt += 1
        elif mv == "L":
            l_cnt += 1
        coords.append((r, c))
    if (r, c) != goal:
        raise ValueError(f"El camino termino en {(r, c)} y no en {goal}")
    if u_cnt != exp_u or l_cnt != exp_l:
        raise ValueError(f"Conteo U={u_cnt}, L={l_cnt} no coincide con U={exp_u}, L={exp_l}")
    return coords


def build_grid(rows: int, cols: int, cell_size: float = 0.85, stroke_opacity: float = 0.55):
    """Construye una rejilla de (rows x cols) intersecciones y su mapa (r, c) -> punto."""
    width = (cols - 1) * cell_size
    height = (rows - 1) * cell_size
    top_left = LEFT * (width / 2) + UP * (height / 2)

    points = {}
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            points[(r, c)] = top_left + RIGHT * ((c - 1) * cell_size) + DOWN * ((r - 1) * cell_size)

    lines = VGroup()
    for r in range(1, rows + 1):
        lines.add(
            Line(
                points[(r, 1)],
                points[(r, cols)],
                stroke_color=TEXT_MUTED,
                stroke_width=1.8,
                stroke_opacity=stroke_opacity,
            )
        )
    for c in range(1, cols + 1):
        lines.add(
            Line(
                points[(1, c)],
                points[(rows, c)],
                stroke_color=TEXT_MUTED,
                stroke_width=1.8,
                stroke_opacity=stroke_opacity,
            )
        )

    dots = VGroup(*[
        Dot(pt, radius=max(0.03, cell_size * 0.055), color=TEXT_MUTED)
        for pt in points.values()
    ])
    return VGroup(lines, dots), points


def build_path_mobject(points: dict, coords: list, color, stroke_width: float = 4.5):
    """Construye el VGroup de segmentos para una lista validada de coordenadas."""
    segs = VGroup()
    for p_from, p_to in zip(coords[:-1], coords[1:]):
        segs.add(
            Line(
                points[p_from],
                points[p_to],
                stroke_color=color,
                stroke_width=stroke_width,
            )
        )
    return segs


def build_mini_grid_card(
    rows: int,
    cols: int,
    coords: list,
    seq_text: str,
    color,
    card_w: float = 2.25,
    card_h: float = 1.85,
    cell_size: float = 0.42,
):
    """Tarjeta compacta con marco, minicuadricula con camino valido y etiqueta."""
    box = RoundedRectangle(
        width=card_w,
        height=card_h,
        corner_radius=0.12,
        stroke_color=color,
        stroke_width=1.6,
        fill_color="#1E2430",
        fill_opacity=0.92,
    )
    grid_mob, pts = build_grid(rows, cols, cell_size=cell_size, stroke_opacity=0.5)
    path_mob = build_path_mobject(pts, coords, color, stroke_width=3.0)
    s_dot = Dot(pts[(1, 1)], radius=0.04, color=ACCENT_MINT)
    g_dot = Dot(pts[(rows, cols)], radius=0.04, color=ACCENT_TERRACOTTA)

    inner_grid = VGroup(grid_mob, path_mob, s_dot, g_dot)
    seq_lbl = formula(seq_text, 16, color)

    content = VGroup(inner_grid, seq_lbl).arrange(DOWN, buff=0.12)
    content.move_to(box.get_center())
    return VGroup(box, content)


class IntuicionCourier(BaseScene):
    def play_validated_path(self, points: dict, coords: list, color, stroke_width: float = 4.5, run_time: float = 1.1):
        """Dibuja un camino validado con un punto guia que viaja de (1, 1) a (R, C)."""
        path_mob = build_path_mobject(points, coords, color, stroke_width=stroke_width)
        tracer = Dot(points[coords[0]], radius=0.085, color=color)
        self.add(tracer)
        self.play(
            Create(path_mob),
            MoveAlongPath(tracer, VMobject().set_points_as_corners([points[p] for p in coords])),
            run_time=run_time,
            rate_func=linear,
        )
        self.remove(tracer)
        return path_mob

    def construct(self):
        # ---------------------------------------------------------
        # 1. Nueva escena: aparece una cuadrícula y se resaltan salida y meta
        # ---------------------------------------------------------
        grid_base, pts_base = build_grid(rows=4, cols=5, cell_size=0.88)
        grid_base.move_to(ORIGIN + DOWN * 0.1)

        start_dot = Dot(pts_base[(1, 1)], radius=0.11, color=ACCENT_MINT)
        start_ring = Circle(radius=0.19, color=ACCENT_MINT, stroke_width=2.0).move_to(pts_base[(1, 1)])
        start_lbl = formula("(1, 1)", 22, ACCENT_MINT).next_to(start_ring, UP + LEFT, buff=0.1)

        goal_dot = Dot(pts_base[(4, 5)], radius=0.11, color=ACCENT_TERRACOTTA)
        goal_ring = Circle(radius=0.19, color=ACCENT_TERRACOTTA, stroke_width=2.0).move_to(pts_base[(4, 5)])
        goal_lbl = formula("(R, C)", 22, ACCENT_TERRACOTTA).next_to(goal_ring, DOWN + RIGHT, buff=0.1)

        self.play(Create(grid_base), run_time=1.0)
        self.play(
            GrowFromCenter(start_dot),
            Create(start_ring),
            FadeIn(start_lbl, shift=DOWN * 0.08),
            GrowFromCenter(goal_dot),
            Create(goal_ring),
            FadeIn(goal_lbl, shift=UP * 0.08),
            run_time=0.9,
        )
        self.wait(0.8)

        # ---------------------------------------------------------
        # 2. Cuadrícula 3x5: caminos válidos que aparecen y se difuminan
        # ---------------------------------------------------------
        self.play(
            FadeOut(grid_base),
            FadeOut(start_dot),
            FadeOut(start_ring),
            FadeOut(start_lbl),
            FadeOut(goal_dot),
            FadeOut(goal_ring),
            FadeOut(goal_lbl),
            run_time=0.5,
        )

        grid_35, pts_35 = build_grid(rows=3, cols=5, cell_size=0.95)
        grid_35.move_to(ORIGIN + DOWN * 0.1)
        s35 = Dot(pts_35[(1, 1)], radius=0.10, color=ACCENT_MINT)
        g35 = Dot(pts_35[(3, 5)], radius=0.10, color=ACCENT_TERRACOTTA)
        header_35 = formula(r"3 \times 5", 24, ACCENT_CYAN).to_edge(UP, buff=0.38)

        self.play(
            Create(grid_35),
            GrowFromCenter(s35),
            GrowFromCenter(g35),
            FadeIn(header_35),
            run_time=0.85,
        )

        # Caso U=0, L=0: un camino directo valido
        moves_00 = ["R", "R", "R", "R", "D", "D"]
        coords_00 = validate_path(3, 5, (1, 1), (3, 5), moves_00, exp_u=0, exp_l=0)
        tag_00 = formula(r"U = 0,\; L = 0", 22, ACCENT_MINT).to_edge(DOWN, buff=0.42)

        self.play(FadeIn(tag_00), run_time=0.35)
        p_00 = self.play_validated_path(pts_35, coords_00, ACCENT_MINT, run_time=1.0)
        self.wait(0.45)
        self.play(FadeOut(p_00), FadeOut(tag_00), run_time=0.5)

        # Caso U=1, L=3: varios caminos validos distintos que aparecen y se difuminan
        tag_13 = formula(r"U = 1,\; L = 3", 22, ACCENT_TERRACOTTA).to_edge(DOWN, buff=0.42)
        self.play(FadeIn(tag_13), run_time=0.35)

        paths_35_13 = [
            (["R", "R", "R", "R", "D", "D", "L", "L", "L", "U", "D", "R", "R", "R"], ACCENT_CYAN),
            (["D", "D", "R", "R", "R", "R", "L", "L", "L", "U", "R", "R", "R", "D"], ACCENT_INDIGO),
            (["R", "D", "R", "R", "R", "D", "L", "L", "U", "L", "R", "R", "D", "R"], ACCENT_MINT),
            (["R", "R", "D", "D", "R", "R", "L", "L", "L", "U", "D", "R", "R", "R"], ACCENT_TERRACOTTA),
        ]

        for mv_list, col in paths_35_13:
            coords_val = validate_path(3, 5, (1, 1), (3, 5), mv_list, exp_u=1, exp_l=3)
            p_mob = self.play_validated_path(pts_35, coords_val, col, run_time=1.05)
            self.wait(0.3)
            self.play(FadeOut(p_mob), run_time=0.45)

        count_msg = label("No basta encontrar uno: hay que contar cuantos existen", 21, TEXT_MAIN).to_edge(DOWN, buff=0.42)
        self.play(FadeOut(tag_13), FadeIn(count_msg), run_time=0.5)
        self.wait(0.75)

        # ---------------------------------------------------------
        # 3. Cuadrícula 2x2: U=0, L=0 -> 2 caminos directos
        # ---------------------------------------------------------
        self.play(
            FadeOut(grid_35),
            FadeOut(s35),
            FadeOut(g35),
            FadeOut(header_35),
            FadeOut(count_msg),
            run_time=0.5,
        )

        grid_22, pts_22 = build_grid(rows=2, cols=2, cell_size=1.45)
        grid_22.move_to(ORIGIN + DOWN * 0.1)
        s22 = Dot(pts_22[(1, 1)], radius=0.11, color=ACCENT_MINT)
        g22 = Dot(pts_22[(2, 2)], radius=0.11, color=ACCENT_TERRACOTTA)
        header_22_00 = formula(r"2 \times 2 \quad \cdot \quad U = 0,\; L = 0", 24, ACCENT_CYAN).to_edge(UP, buff=0.38)

        self.play(
            Create(grid_22),
            GrowFromCenter(s22),
            GrowFromCenter(g22),
            FadeIn(header_22_00),
            run_time=0.8,
        )

        direct_cases = [
            (["R", "D"], "Derecha, Abajo", ACCENT_MINT),
            (["D", "R"], "Abajo, Derecha", ACCENT_CYAN),
        ]

        active_lbl = None
        for mv_list, desc_txt, col in direct_cases:
            coords_val = validate_path(2, 2, (1, 1), (2, 2), mv_list, exp_u=0, exp_l=0)
            new_lbl = label(desc_txt, 22, col).to_edge(DOWN, buff=0.48)
            if active_lbl is not None:
                self.play(FadeOut(active_lbl), run_time=0.25)
            self.play(FadeIn(new_lbl), run_time=0.3)
            active_lbl = new_lbl

            p_mob = self.play_validated_path(pts_22, coords_val, col, stroke_width=5.0, run_time=0.95)
            self.wait(0.35)
            self.play(FadeOut(p_mob), run_time=0.4)

        if active_lbl is not None:
            self.play(FadeOut(active_lbl), run_time=0.25)

        two_ways_lbl = formula(r"\text{Total} = 2\text{ caminos}", 25, ACCENT_MINT).to_edge(DOWN, buff=0.42)
        self.play(FadeIn(two_ways_lbl, scale=0.92), run_time=0.55)
        self.wait(0.75)

        # ---------------------------------------------------------
        # 4. Cuadrícula 2x2: U=1, L=0 -> 4 caminos con flecha y miniatura
        # ---------------------------------------------------------
        self.play(
            FadeOut(grid_22),
            FadeOut(s22),
            FadeOut(g22),
            FadeOut(header_22_00),
            FadeOut(two_ways_lbl),
            run_time=0.5,
        )

        header_22_10 = formula(r"2 \times 2 \quad \cdot \quad U = 1,\; L = 0", 24, ACCENT_TERRACOTTA).to_edge(UP, buff=0.38)

        main_grid, main_pts = build_grid(rows=2, cols=2, cell_size=1.35)
        # main_grid.move_to(LEFT * 3.85 + DOWN * 0.1)
        grid_shift = LEFT * 3.85 + DOWN * 0.1
        main_grid.move_to(grid_shift)
        main_pts = {k: pt + grid_shift for k, pt in main_pts.items()}
        
        m_start = Dot(main_pts[(1, 1)], radius=0.10, color=ACCENT_MINT)
        m_goal = Dot(main_pts[(2, 2)], radius=0.10, color=ACCENT_TERRACOTTA)

        # 4 tarjetas fijas a la derecha (2x2) para las miniaturas
        slot_centers = [
            RIGHT * 1.45 + UP * 1.15,
            RIGHT * 4.15 + UP * 1.15,
            RIGHT * 1.45 + DOWN * 1.25,
            RIGHT * 4.15 + DOWN * 1.25,
        ]
        slot_placeholders = VGroup(*[
            RoundedRectangle(
                width=2.25,
                height=1.85,
                corner_radius=0.12,
                stroke_color=TEXT_MUTED,
                stroke_width=1.2,
                stroke_opacity=0.45,
                fill_color="#1E2430",
                fill_opacity=0.5,
            ).move_to(pos)
            for pos in slot_centers
        ])

        counter_mob = formula(r"\text{Conteo}: 0 / 4", 22, TEXT_MAIN).to_edge(DOWN, buff=0.38)

        self.play(
            FadeIn(header_22_10),
            Create(main_grid),
            GrowFromCenter(m_start),
            GrowFromCenter(m_goal),
            FadeIn(slot_placeholders),
            FadeIn(counter_mob),
            run_time=0.85,
        )

        four_valid_paths = [
            (["D", "U", "D", "R"], "D - U - D - R", ACCENT_CYAN),
            (["D", "U", "R", "D"], "D - U - R - D", ACCENT_MINT),
            (["D", "R", "U", "D"], "D - R - U - D", ACCENT_INDIGO),
            (["R", "D", "U", "D"], "R - D - U - D", ACCENT_TERRACOTTA),
        ]

        prev_path = None
        for idx, (mv_list, seq_str, col) in enumerate(four_valid_paths):
            coords_val = validate_path(2, 2, (1, 1), (2, 2), mv_list, exp_u=1, exp_l=0)

            if prev_path is not None:
                self.play(FadeOut(prev_path), run_time=0.25)

            curr_path = self.play_validated_path(
                main_pts,
                coords_val,
                col,
                stroke_width=4.8,
                run_time=0.95,
            )
            prev_path = curr_path

            target_center = slot_centers[idx]
            arrow_mob = Arrow(
                main_grid.get_right() + RIGHT * 0.12,
                target_center + LEFT * 1.18,
                buff=0.05,
                stroke_color=col,
                stroke_width=2.8,
                max_tip_length_to_length_ratio=0.22,
            )

            mini_card = build_mini_grid_card(
                rows=2,
                cols=2,
                coords=coords_val,
                seq_text=seq_str,
                color=col,
                card_w=2.25,
                card_h=1.85,
                cell_size=0.40,
            ).move_to(target_center)

            new_counter = formula(rf"\text{{Conteo}}: {idx + 1} / 4", 22, ACCENT_MINT).to_edge(DOWN, buff=0.38)

            self.play(
                GrowArrow(arrow_mob),
                FadeIn(mini_card, scale=0.88),
                FadeOut(counter_mob),
                FadeIn(new_counter),
                run_time=0.75,
            )
            counter_mob = new_counter
            self.play(FadeOut(arrow_mob), run_time=0.25)
            self.wait(0.25)

        if prev_path is not None:
            self.play(FadeOut(prev_path), run_time=0.3)

        # ---------------------------------------------------------
        # 5. Espera de 3s tras terminar todo y animación de salida
        # ---------------------------------------------------------
        self.wait(3.0)

        self.play(
            FadeOut(Group(*self.mobjects), shift=DOWN * 0.2, scale=0.96),
            run_time=1.0,
        )
        self.wait(0.3)