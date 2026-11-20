"""Plecas estilo noticiero sobre fondo verde (Chroma Key) con estética Modern Flat."""
from manim import *
from theme import (
    BG_COLOR,
    TEXT_MAIN,
    ACCENT_CYAN,
    ACCENT_MINT,
    ACCENT_INDIGO,
    ACCENT_TERRACOTTA,
)

CHROMA_GREEN = "#00FF00"


class PlecaBase(Scene):
    """Escena base reutilizable para plecas de nombre y cargo."""

    TITLE_TEXT: str = r"Cargo o Institución"
    NAME_TEXT: str = r"Nombre de la Persona"
    ACCENT_COLOR: str = ACCENT_CYAN
    HOLD_TIME: float = 15.0

    def setup(self):
        self.camera.background_color = CHROMA_GREEN

    def construct(self):
        # 1. Tipografía en LaTeX: primero título (acento), debajo nombre (blanco bold)
        title_mob = Tex(
            self.TITLE_TEXT,
            font_size=18,
            color=self.ACCENT_COLOR,
        )
        name_mob = Tex(
            rf"\textbf{{{self.NAME_TEXT}}}",
            font_size=28,
            color=TEXT_MAIN,
        )

        # Limitar ancho máximo para pantallas 16:9 manteniendo proporción
        max_text_w = 10.2
        if title_mob.width > max_text_w:
            title_mob.scale_to_fit_width(max_text_w)
        if name_mob.width > max_text_w:
            name_mob.scale_to_fit_width(max_text_w)

        text_block = VGroup(title_mob, name_mob).arrange(
            DOWN,
            buff=0.12,
            aligned_edge=LEFT,
        )

        # 2. Dimensiones dinámicas de la tarjeta oscura
        pad_x = 0.34
        pad_y = 0.24
        card_w = max(4.6, text_block.width + pad_x * 2)
        card_h = text_block.height + pad_y * 2

        card_bg = RoundedRectangle(
            width=card_w,
            height=card_h,
            corner_radius=0.10,
            fill_color=BG_COLOR,
            fill_opacity=0.96,
            stroke_color=self.ACCENT_COLOR,
            stroke_width=1.4,
        )

        # Barra vertical lateral de acento estilo broadcast
        accent_bar = RoundedRectangle(
            width=0.09,
            height=card_h,
            corner_radius=0.04,
            fill_color=self.ACCENT_COLOR,
            fill_opacity=1.0,
            stroke_width=0,
        )
        accent_bar.move_to(card_bg.get_left() + RIGHT * 0.045)

        text_block.move_to(card_bg.get_left() + RIGHT * (pad_x + 0.06), aligned_edge=LEFT)

        # 3. Posición segura tipo noticiero (abajo a la izquierda con margen)
        anchor_point = LEFT * 6.0 + DOWN * 2.55
        full_banner = VGroup(card_bg, accent_bar, text_block)
        full_banner.move_to(anchor_point, aligned_edge=LEFT + DOWN)

        # 4. Animación de entrada escalonada
        self.play(
            GrowFromCenter(accent_bar),
            run_time=0.45,
        )
        self.play(
            FadeIn(card_bg, shift=RIGHT * 0.25),
            run_time=0.65,
        )
        self.play(
            FadeIn(title_mob, shift=DOWN * 0.08),
            run_time=0.40,
        )
        self.play(
            FadeIn(name_mob, shift=UP * 0.10),
            run_time=0.55,
        )

        # 5. Tiempo en pantalla
        self.wait(self.HOLD_TIME)

        # 6. Animación de salida limpia hacia el chroma
        self.play(
            FadeOut(name_mob, shift=DOWN * 0.08),
            FadeOut(title_mob, shift=UP * 0.06),
            run_time=0.55,
        )
        self.play(
            FadeOut(card_bg, shift=LEFT * 0.25),
            ShrinkToCenter(accent_bar),
            run_time=0.60,
        )
        self.wait(0.2)


# =====================================================================
# Escenas individuales listas para renderizar
# =====================================================================


# ENTRENADORES
class PlecaCarlosSegura(PlecaBase):
    TITLE_TEXT = r"Investigador del CIMAT $\cdot$ Profesor UG $\cdot$ Coach UG--CIMAT"
    NAME_TEXT = r"Dr. Carlos Segura González"
    ACCENT_COLOR = ACCENT_TERRACOTTA


class PlecaMariaRosario(PlecaBase):
    TITLE_TEXT = r"Subdirectora Académica $\cdot$ ESCOM--IPN"
    NAME_TEXT = r"Ing. María del Rosario Galeana Chávez"
    ACCENT_COLOR = ACCENT_INDIGO


class PlecaRafaelNorman(PlecaBase):
    TITLE_TEXT = r"Profesor $\cdot$ ESCOM--IPN"
    NAME_TEXT = r"Ing. Rafael Norman Saucedo Delgado"
    ACCENT_COLOR = ACCENT_INDIGO


class PlecaEdgardoFranco(PlecaBase):
    TITLE_TEXT = r"Profesor y Coach $\cdot$ ESCOM--IPN"
    NAME_TEXT = r"Ing. Edgardo Adrián Franco Martínez"
    ACCENT_COLOR = ACCENT_INDIGO

# EMPRESAS

class PlecaRamiroGarcia(PlecaBase):
    TITLE_TEXT = r"Development Manager at Oracle"
    NAME_TEXT = r"Ing. Ramiro García Zepeda"
    ACCENT_COLOR = ACCENT_CYAN


class PlecaAlexaValls(PlecaBase):
    TITLE_TEXT = r"Equipo de Talento $\cdot$ Primero IA"
    NAME_TEXT = r"Lic. Alexa Valls"
    ACCENT_COLOR = ACCENT_CYAN

class PlecaCantilever(PlecaBase):
    TITLE_TEXT = r"Cantilever $\cdot$ Ingeniería y Desarrollo"
    NAME_TEXT = r"Tecnología Mexicana para el Sector Energético"
    ACCENT_COLOR = ACCENT_CYAN


# guillot

class PlecaGuillot(PlecaBase):
    TITLE_TEXT = r"Director Regional $\cdot$ ICPC México"
    NAME_TEXT = r"Mtro. Carlos Alberto Fernández Guillot"
    ACCENT_COLOR = ACCENT_MINT