"""
Miniaturas ICPC México 2026 (Manim Community Edition)
=====================================================

Clases (una miniatura cada una) y la foto que usa cada una:

    Thumb5Horas   ->  img3.JPG   "5 HORAS"
    ThumbSTEM     ->  img1.JPG   "¿MÁS LEJOS EN STEM?"  + equipo · estrategia · resiliencia
    Thumb10de12   ->  img3.JPG   "10 DE 12"

Las imágenes deben estar en la MISMA carpeta que este archivo (no importan las
mayúsculas de la extensión: .JPG, .jpg, .png...). Si falta alguna, se dibuja un
marcador y el código sigue funcionando.

PARÁMETROS QUE PUEDES MOVER (al inicio de cada clase):

    DESPLAZAR_X   Solo traslada la foto, sin zoom. Fracción del ancho del cuadro:
                  +0.10 la mueve 10 % a la DERECHA, -0.10 a la izquierda.
    DESPLAZAR_Y   Igual en vertical: +0.10 la sube, -0.10 la baja.
    ZOOM          1.0 = tamaño base. Solo cambia si TÚ lo cambias (1.2 = 20 % más cerca).

    Al mover la foto puede aparecer una franja vacía del color de fondo. En las dos
    primeras miniaturas, mover a la derecha deja esa franja bajo el degradado oscuro
    (no se nota); mover a la izquierda sí la muestra: ahí sube ZOOM un poco.

Render (PNG de 1280x720, un solo fotograma):

    manim -s -r 1280,720 thumbnails_icpc.py Thumb5Horas
    manim -s -r 1280,720 thumbnails_icpc.py ThumbSTEM
    manim -s -r 1280,720 thumbnails_icpc.py Thumb10de12
    manim -s -a -r 1280,720 thumbnails_icpc.py          # todas a la vez

Salida: media/images/thumbnails_icpc/

Tipografía: letras LaTeX (Computer Modern, el estilo clásico de Manim). Requiere tener
LaTeX instalado (TeX Live / MiKTeX). Si no se detecta, usa un texto normal como respaldo.
Puedes forzarlo cambiando USAR_LATEX más abajo.
"""

import shutil
from pathlib import Path

import numpy as np
from manim import *
from PIL import Image, ImageDraw, ImageOps

# ── Paleta Slate con roles fijos ───────────────────────────────────────────────
BG = "#181C24"          # fondo
PANEL = "#232936"       # tarjetas / marcadores
MENTA = "#2DD4BF"       # idea correcta, resultado, acento
TERRACOTA = "#D97706"   # tiempo, presión
INDIGO = "#6366F1"      # equipo
VINO = "#C0392B"        # error, lo que falta
TEXT = "#F1F4F9"
MUTED = "#C8D0DE"
GRAY = "#5B667A"
PANEL_RGBA = (35, 41, 54, 255)

# None = automático (usa LaTeX si está instalado); True / False para forzar.
USAR_LATEX = None
if USAR_LATEX is None:
    USAR_LATEX = shutil.which("latex") is not None

# Fuentes de respaldo si no hay LaTeX
SERIF_FB = "CMU Serif"
MONO_FB = "CMU Typewriter Text"

config.background_color = BG
HERE = Path(__file__).resolve().parent
EXTENSIONES = {".png", ".jpg", ".jpeg", ".webp"}


# ── Utilidades ─────────────────────────────────────────────────────────────────
def tx(parts, color=TEXT, mono=False, width=None, height=None):
    """Texto estilo clásico de Manim (LaTeX, negritas Computer Modern).

    parts: un string, o una lista [("¿MÁS", TEXT), ("LEJOS", MENTA)] para colorear partes
           de una misma línea (mantiene la línea base alineada).
    mono:  True usa tipo máquina de escribir (\\texttt), útil para etiquetas pequeñas.
    width / height: tamaño objetivo en unidades de Manim.
    """
    if isinstance(parts, str):
        parts = [(parts, color)]

    if USAR_LATEX:
        cmd = r"\texttt" if mono else r"\textbf"
        tex = [cmd + "{" + s.replace("·", r"$\cdot$") + "}" for s, _ in parts]
        t = Tex(*tex, arg_separator=" ", color=color)
        for sub, (_, c) in zip(t, parts):
            sub.set_color(c)
    else:
        full = " ".join(s for s, _ in parts)
        t2c = {s: c for s, c in parts if c != color}
        t = Text(full, font=MONO_FB if mono else SERIF_FB, weight="BOLD",
                 color=color, font_size=48, t2c=t2c)

    if width is not None:
        t.scale_to_fit_width(width)
    if height is not None:
        t.scale_to_fit_height(height)
    return t


def buscar_imagen(name):
    """Ruta de la imagen (ignora mayúsculas/minúsculas y la extensión exacta). None si no existe."""
    p = HERE / name
    if p.exists():
        return p
    stem = Path(name).stem.lower()
    for f in HERE.iterdir():
        if f.is_file() and f.stem.lower() == stem and f.suffix.lower() in EXTENSIONES:
            return f
    return None


def abrir(path, max_px=3840):
    """Abre la foto respetando la orientación EXIF del celular/cámara y la reduce si es enorme."""
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGBA")
    im.thumbnail((max_px, max_px), Image.LANCZOS)
    return im


def placeholder(name, width, height):
    """Marcador punteado para cuando la imagen no existe."""
    box = DashedVMobject(
        RoundedRectangle(corner_radius=0.3, width=width, height=height,
                         stroke_color=GRAY, stroke_width=4),
        num_dashes=80,
    )
    label = tx(f"[{name}]", color=GRAY, mono=True, height=0.3)
    return VGroup(box, label)


def photo_cover(name, dx=0.0, dy=0.0, zoom=1.0):
    """Foto que cubre el cuadro. Solo se TRASLADA: dx, dy como fracción del cuadro
    (+dx = derecha, +dy = arriba). El zoom es el que tú indiques, nunca automático."""
    path = buscar_imagen(name)
    if path is None:
        fondo = Rectangle(width=config.frame_width, height=config.frame_height,
                          fill_color=PANEL, fill_opacity=1, stroke_width=0)
        etiqueta = tx(f"[{name}]", color=GRAY, mono=True, height=0.3)
        etiqueta.to_edge(RIGHT, buff=2.5)
        return VGroup(fondo, etiqueta)

    img = ImageMobject(np.array(abrir(path)))
    img.scale_to_fit_height(config.frame_height)
    if img.width < config.frame_width:
        img.scale_to_fit_width(config.frame_width)
    img.scale(zoom)
    return img.move_to(ORIGIN).shift(
        RIGHT * dx * config.frame_width + UP * dy * config.frame_height
    )


def fade_izquierda(solid=0.5, end=0.88, w=960, h=540):
    """Degradado del color de fondo: opaco hasta `solid` (fracción del ancho) y transparente en `end`.
    Sirve para que el texto de la izquierda se lea sobre cualquier foto."""
    x = np.linspace(0, 1, w)
    a = np.clip((end - x) / (end - solid), 0, 1)
    a = a * a * (3 - 2 * a)  # smoothstep
    arr = np.zeros((h, w, 4), dtype=np.uint8)
    arr[..., 0], arr[..., 1], arr[..., 2] = 24, 28, 36
    arr[..., 3] = (a * 255).astype(np.uint8)[None, :]
    m = ImageMobject(arr)
    m.scale_to_fit_height(config.frame_height)
    return m.move_to(ORIGIN)


def rounded_photo(name, width, height, radius=0.3, dx=0.0, dy=0.0, zoom=1.0, ppu=150):
    """Foto dentro de un marco con esquinas redondeadas. Solo se TRASLADA dentro del marco:
    dx, dy como fracción del marco (+dx = derecha, +dy = arriba). Lo que quede vacío se rellena
    con el color de panel."""
    path = buscar_imagen(name)
    if path is None:
        return placeholder(name, width, height)

    W, H = int(width * ppu), int(height * ppu)
    im = abrir(path)
    iw, ih = im.size
    s = max(W / iw, H / ih) * zoom                      # misma escala base que 'cover'
    im = im.resize((int(iw * s), int(ih * s)), Image.LANCZOS)

    canvas = Image.new("RGBA", (W, H), PANEL_RGBA)
    ox = (W - im.width) // 2 + int(round(dx * W))
    oy = (H - im.height) // 2 - int(round(dy * H))
    canvas.paste(im, (ox, oy))

    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, W - 1, H - 1), radius=int(radius * ppu), fill=255)
    canvas.putalpha(mask)
    m = ImageMobject(np.array(canvas))
    m.scale_to_fit_width(width)
    return m


def pill(label, color):
    """Etiqueta redondeada con borde de color."""
    t = tx(label, color=color, mono=True, height=0.34)
    box = RoundedRectangle(corner_radius=0.18, width=t.width + 0.7, height=t.height + 0.5,
                           stroke_color=color, stroke_width=4,
                           fill_color=BG, fill_opacity=0.85)
    t.move_to(box)
    return VGroup(box, t)


# ── 1. "5 HORAS" ───────────────────────────────────────────────────────────────
class Thumb5Horas(Scene):
    FOTO = "img3.JPG"
    DESPLAZAR_X = 0.08     # +0.10 = foto 10 % a la derecha (sin zoom)
    DESPLAZAR_Y = 0.0
    ZOOM = 1.0

    def construct(self):
        self.add(photo_cover(self.FOTO, self.DESPLAZAR_X, self.DESPLAZAR_Y, self.ZOOM))
        self.add(fade_izquierda(solid=0.5, end=0.88))

        titulo = tx("5 HORAS", width=8.6)
        reloj = tx("05:00:00", color=TERRACOTA, width=5.6)
        sub = tx("3 PERSONAS · 1 COMPUTADORA", color=MUTED, mono=True, width=6.0)

        bloque = VGroup(titulo, reloj, sub).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        bloque.move_to(ORIGIN).to_edge(LEFT, buff=0.8)
        self.add(bloque)


# ── 2. "¿MÁS LEJOS EN STEM?" ───────────────────────────────────────────────────
class ThumbSTEM(Scene):
    FOTO = "img1.JPG"
    DESPLAZAR_X = 0.3
    DESPLAZAR_Y = 0.0
    ZOOM = 1.0
    # Versión larga (más palabras, menos legible en celular):
    # LINEA1 = [("¿QUIERES", TEXT), ("LLEGAR", TEXT)];  LINEA2 = [("MÁS", TEXT), ("LEJOS", MENTA), ("EN STEM?", TEXT)]
    LINEA1 = [("¿MÁS", TEXT), ("LEJOS", MENTA)]
    LINEA2 = [("EN STEM?", TEXT)]

    def construct(self):
        self.add(photo_cover(self.FOTO, self.DESPLAZAR_X, self.DESPLAZAR_Y, self.ZOOM))
        self.add(fade_izquierda(solid=0.5, end=0.9))

        titulo = VGroup(tx(self.LINEA1), tx(self.LINEA2)).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        titulo.scale_to_fit_width(8.4)

        fila = VGroup(
            pill("EQUIPO", INDIGO),         # equipo = índigo
            pill("ESTRATEGIA", MENTA),      # idea = menta
            pill("RESILIENCIA", TERRACOTA)  # presión = terracota
        ).arrange(RIGHT, buff=0.25)
        fila.scale_to_fit_width(min(8.4, fila.width))

        bloque = VGroup(titulo, fila).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        bloque.move_to(ORIGIN).to_edge(LEFT, buff=0.8)
        self.add(bloque)


# ── 3. "10 DE 12" ──────────────────────────────────────────────────────────────
class Thumb10de12(Scene):
    FOTO = "img3.JPG"
    DESPLAZAR_X = -0.48     # +0.10 = foto 10 % del ancho del marco a la derecha (sin zoom)
    DESPLAZAR_Y = 0.0
    ZOOM = 1.0
    RESUELTOS, TOTAL = 10, 12   # confirma estas cifras con el marcador final

    def construct(self):
        etiqueta = tx("ICPC MÉXICO 2026", color=TERRACOTA, mono=True, height=0.34)
        etiqueta.to_corner(UL, buff=0.7)

        diez = tx(str(self.RESUELTOS), color=MENTA, height=3.0)
        de = tx(f"DE {self.TOTAL}", height=1.05)
        bloque = VGroup(diez, de).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        bloque.move_to(ORIGIN).to_edge(LEFT, buff=0.8)

        cuadros = VGroup()
        for i in range(self.TOTAL):
            if i < self.RESUELTOS:
                c = RoundedRectangle(corner_radius=0.06, width=0.44, height=0.44,
                                     fill_color=MENTA, fill_opacity=1, stroke_width=0)
            else:
                c = RoundedRectangle(corner_radius=0.06, width=0.36, height=0.36,
                                     stroke_color=VINO, stroke_width=5, fill_opacity=0)
            cuadros.add(c)
        cuadros.arrange(RIGHT, buff=0.11).to_corner(DL, buff=0.7)

        foto = rounded_photo(self.FOTO, width=5.2, height=6.7,
                             dx=self.DESPLAZAR_X, dy=self.DESPLAZAR_Y, zoom=self.ZOOM)
        foto.to_edge(RIGHT, buff=0.8)

        self.add(foto, etiqueta, bloque, cuadros)