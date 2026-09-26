"""Reusable visual components for the binary exponentiation scenes."""
from pathlib import Path
import sys

from manim import DOWN, UP, VGroup, Tex, MathTex, RoundedRectangle

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from styles.theme import (  # noqa: E402
    ACCENT_CYAN,
    ACCENT_INDIGO,
    ACCENT_MINT,
    ACCENT_TERRACOTTA,
    ACCENT_VINO,
    BG_COLOR,
    TEXT_MAIN,
    TEXT_MUTED,
)

COLOR_FORCE_BRUTE = ACCENT_VINO
COLOR_OPTIMAL = ACCENT_MINT
COLOR_EXPOS = ACCENT_TERRACOTTA
COLOR_MODULO = ACCENT_INDIGO
COLOR_CYAN = ACCENT_CYAN
PANEL_COLOR = "#11141A"
MODULUS = 10**9 + 7


def escape_tex(text: str) -> str:
    """Escape literal prose/code once, including symbols unsupported by pdfLaTeX."""
    replacements = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%",
        "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
        "×": r"\ensuremath{\times}", "→": r"\ensuremath{\rightarrow}",
        "·": r"\ensuremath{\cdot}", "<": r"\textless{}", ">": r"\textgreater{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def label(text: str, size: float = 28, color: str = TEXT_MAIN) -> Tex:
    # LaTeX's glyph metrics are smaller; retain the original visual hierarchy.
    return Tex(escape_tex(text) if text else r"\strut", font_size=size * 1.5, color=color)


def heading(number: int, text: str) -> VGroup:
    eyebrow = label(f"EXPONENCIACIÓN BINARIA  /  {number:02d}", 16, COLOR_CYAN)
    title = label(text, 36)
    return VGroup(eyebrow, title).arrange(DOWN, buff=0.18).to_edge(UP, buff=0.35)


def formula(tex: str, size: float = 42, color: str = TEXT_MAIN) -> MathTex:
    return MathTex(tex, font_size=size, color=color)


def card(title: str, value: str, color: str, width: float = 5.2) -> VGroup:
    box = RoundedRectangle(width=width, height=1.65, corner_radius=0.16,
                           stroke_color=color, fill_color=PANEL_COLOR, fill_opacity=1)
    value_mobject = formula(value, 35) if value.isdecimal() else label(value, 35)
    words = VGroup(label(title, 21, color), value_mobject).arrange(DOWN, buff=0.22)
    if words.width > width - 0.4:
        words.scale_to_fit_width(width - 0.4)
    return VGroup(box, words)


def bit_row(bits: str = "11001") -> VGroup:
    cells = VGroup()
    for bit in bits:
        color = COLOR_OPTIMAL if bit == "1" else TEXT_MUTED
        box = RoundedRectangle(width=0.95, height=0.85, corner_radius=0.1,
                               stroke_color=COLOR_MODULO, fill_color=PANEL_COLOR,
                               fill_opacity=1)
        cells.add(VGroup(box, formula(bit, 34, color)))
    return cells.arrange(buff=0.25)
