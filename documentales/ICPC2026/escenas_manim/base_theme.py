"""Sistema de layout, tipografía y paleta basado exclusivamente en theme.py."""
from manim import *
import re
from theme import (BG_COLOR, TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT,
                   ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN)

TITLE_SIZE = 36
BODY_SIZE = 28
LABEL_SIZE = 23
SMALL_SIZE = 19
STROKE = 2.4
THIN = 1.35


def escape_tex(text):
    replacements = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
        "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def label(text, size=LABEL_SIZE, color=TEXT_MAIN, width=None):
    """Plain-language label rendered by LaTeX; accepts newlines as line breaks."""
    content = r" \\ ".join(escape_tex(part) for part in str(text).splitlines())
    mob = Tex(content, font_size=size, color=color)
    if width is not None and mob.width > width:
        mob.scale_to_fit_width(width)
    return mob


def formula(source, size=BODY_SIZE, color=TEXT_MAIN):
    return MathTex(source, font_size=size, color=color)


class BaseScene(Scene):
    def setup(self):
        super().setup()
        self.camera.background_color = BG_COLOR

    def title(self, text):
        obj = label(text, TITLE_SIZE, TEXT_MAIN, width=12.5)
        obj.to_edge(UP, buff=0.3)
        return obj

    def pause(self, duration=1.25):
        self.wait(duration)

    def clear_scene(self, run_time=0.55):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=run_time)
        self.wait(0.25)


def card(text, width=3.0, height=1.15, accent=ACCENT_CYAN, size=LABEL_SIZE):
    frame = RoundedRectangle(width=width, height=height, corner_radius=0.12,
                             stroke_color=accent, stroke_width=STROKE,
                             fill_color=BG_COLOR, fill_opacity=1)
    copy = label(text, size=size, color=TEXT_MAIN, width=width - 0.3)
    if copy.height > height - 0.18:
        copy.scale_to_fit_height(height - 0.18)
    return VGroup(frame, copy.move_to(frame))


def grid_graph(rows=1, cols=1, cell=1.2, color=ACCENT_CYAN):
    """Street-grid vertices are indexed from top-left, matching the statement."""
    x0, y0 = -cols * cell / 2, rows * cell / 2
    lines = VGroup()
    for r in range(rows + 1):
        y = y0 - r * cell
        lines.add(Line([x0, y, 0], [x0 + cols * cell, y, 0], color=color, stroke_width=THIN))
    for c in range(cols + 1):
        x = x0 + c * cell
        lines.add(Line([x, y0, 0], [x, y0 - rows * cell, 0], color=color, stroke_width=THIN))
    points = {(r, c): np.array([x0 + c * cell, y0 - r * cell, 0])
              for r in range(rows + 1) for c in range(cols + 1)}
    nodes = VGroup(*[Dot(point, radius=0.045, color=TEXT_MAIN) for point in points.values()])
    return VGroup(lines, nodes), points
