"""
paper_theme.py -- Identidad visual "papel y tinta" para Another Math Channel.
Colócalo en styles/theme.py (o junto a tus escenas) y haz: from paper_theme import *
"""
from manim import *

# ----------------------------------------------------------------------
# PALETA
# ----------------------------------------------------------------------
PAPER = "#F7F6F1"       # fondo: papel cálido, no blanco puro
INK = "#1B1B1F"         # tinta principal (casi negro, menos agresivo que #000)
INK_SOFT = "#4B4B53"    # tinta secundaria: ejes, anotaciones, texto de apoyo
GRAPHITE = "#8C8C92"    # estructura: elementos de contexto / fondo
RULE = "#D8D5CB"        # cuadrícula tipo papel milimetrado
ACCENT = "#B1262B"      # carmín: UN solo foco por escena


class SW:
    """Grosores de trazo (stroke_width de Manim)."""
    GRID = 0.8
    HAIR = 1.2       # filetes finos, marcos interiores
    AUX = 1.8        # líneas auxiliares (punteadas)
    AXIS = 2.0
    FRAME = 2.5      # marcos, aristas de grafos
    CURVE = 3.5      # funciones / objeto principal
    ACCENT = 4.5     # trazo de acento
    EMPHASIS = 5.0   # máximo énfasis en tinta


class FS:
    """Tamaños de fuente (para frame 16 x 9, 1080p/1440p)."""
    TITLE = 56
    HEAD = 44
    BODY = 36
    NOTE = 28
    MICRO = 22       # mínimo legible en video


# ----------------------------------------------------------------------
# ESCENA BASE
# ----------------------------------------------------------------------
class PaperScene(Scene):
    def setup(self):
        super().setup()
        self.camera.background_color = PAPER


# ----------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------
def tex(s, size=FS.BODY, color=INK, **kw):
    return MathTex(s, font_size=size, color=color, **kw)


def node(pos, filled=True, r=0.08, stroke=SW.FRAME):
    """Relleno = dato / conocido. Hueco = incógnita / variable."""
    d = Dot(pos, radius=r, color=INK)
    if not filled:
        d.set_fill(PAPER, 1).set_stroke(INK, stroke)
    return d


def edge(a, b, dashed=False, stroke=SW.FRAME, color=INK):
    """Sólida = relación establecida. Punteada = auxiliar / hipotética."""
    if dashed:
        return DashedLine(a, b, stroke_color=color, stroke_width=stroke, dash_length=0.12)
    return Line(a, b, stroke_color=color, stroke_width=stroke)


def pen_axes(x_range, y_range, x_length, y_length, **kw):
    return Axes(
        x_range=x_range, y_range=y_range, x_length=x_length, y_length=y_length,
        axis_config={"stroke_color": INK_SOFT, "stroke_width": SW.AXIS, "include_tip": True,
                     "tip_width": 0.12, "tip_height": 0.12},
        **kw,
    )
