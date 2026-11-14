"""Bloque 5 y cierre: boletos, restricciones y entrevistas."""
from manim import *
from base_theme import BaseScene, card, label, formula
from theme import TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT, ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN
from sc30_final import TOP25


class AvanceLATAM(BaseScene):
    def construct(self):
        self.play(Write(self.title("La clasificación conduce al LATAM")))
        left = card("TABLA\nNACIONAL", 3.2, 1.65, ACCENT_CYAN, 24).move_to(LEFT * 4.1 + UP * 0.2)
        right = card("LATAM\nCHAMPIONSHIP", 3.6, 1.65, ACCENT_MINT, 23).move_to(RIGHT * 4.0 + UP * 0.2)
        path = Arrow(left.get_right(), right.get_left(), color=ACCENT_MINT, stroke_width=3.0, buff=0.18)
        expectation = label("avanzan los mejores lugares", 22, TEXT_MUTED).move_to(UP * 1.65)
        self.play(FadeIn(left), FadeIn(right), FadeIn(expectation), GrowArrow(path), run_time=1.0)
        self.wait(1.1)
        interruption = label("NO SIEMPRE", 31, ACCENT_VINO).move_to(DOWN * 1.45)
        broken = VGroup(Line(path.get_start(), path.get_center() + LEFT * 0.12,
                             color=ACCENT_VINO, stroke_width=3.0),
                        Line(path.get_center() + RIGHT * 0.12, path.get_end(),
                             color=ACCENT_VINO, stroke_width=3.0))
        self.play(FadeOut(path), Create(broken), FadeIn(interruption), run_time=0.8)
        self.wait(1.8)


class ComparacionPuestos(BaseScene):
    def construct(self):
        self.play(Write(self.title("Puestos y boletos pueden diferir")))
        headers = [label("PUESTOS 15–19", 22, ACCENT_VINO),
                   label("PUESTOS 21–25", 22, ACCENT_MINT)]
        headers[0].move_to(LEFT * 3.1 + UP * 1.8)
        headers[1].move_to(RIGHT * 3.1 + UP * 1.8)
        data = [("7 problemas", "No clasificaron", ACCENT_VINO),
                ("6 problemas", "Sí clasificaron", ACCENT_MINT)]
        groups = []
        for idx, (solved, status, color) in enumerate(data):
            title = headers[idx]
            amount = formula(r"7" if idx == 0 else r"6", 54, color)
            solved_label = label("problemas resueltos", 21, TEXT_MUTED)
            state = label(status, 24, color)
            group = VGroup(amount, solved_label, state).arrange(DOWN, buff=0.35)
            group.move_to((LEFT if idx == 0 else RIGHT) * 3.1 + DOWN * 0.05)
            groups.append(group)
        divider = DashedLine(UP * 1.4, DOWN * 1.7, color=TEXT_MUTED)
        self.play(FadeIn(VGroup(*headers)), Create(divider), run_time=0.8)
        self.play(FadeIn(groups[0]), FadeIn(groups[1]), run_time=0.9)
        foot = label("El lugar 20 también tiene 7 problemas; la comparación estricta es con 21–25.",
                     18, TEXT_MUTED, width=11.8).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(foot), run_time=0.7)
        self.wait(2.2)


class FactoresLogisticos(BaseScene):
    def construct(self):
        self.play(Write(self.title("La selección considera varias reglas")))
        names = [("desempeño", ACCENT_CYAN), ("cuota regional", ACCENT_INDIGO),
                 ("cupo por institución", ACCENT_TERRACOTTA), ("estatus de sede", ACCENT_VINO)]
        cards = VGroup(*[card(name, 2.65, 1.0, color, 20) for name, color in names])
        cards.arrange(RIGHT, buff=0.25).move_to(UP * 0.55)
        bracket = Brace(cards, DOWN, color=TEXT_MUTED, buff=0.18)
        gate = card("SELECCIÓN\nFINAL", 3.4, 1.2, ACCENT_MINT, 23).move_to(DOWN * 1.55)
        arrow = Arrow(bracket.get_bottom(), gate.get_top(), color=ACCENT_MINT, buff=0.15, stroke_width=2.5)
        self.play(LaggedStart(*[FadeIn(item) for item in cards], lag_ratio=0.15), run_time=1.2)
        self.play(GrowFromCenter(bracket), GrowArrow(arrow), FadeIn(gate), run_time=1.0)
        self.wait(2.0)


class Reconocimiento(BaseScene):
    def construct(self):
        self.play(Write(self.title("Reconocimiento al esfuerzo de todos")))
        words = VGroup(label("ESFUERZO", 28, TEXT_MAIN),
                       label("EQUIPO", 28, ACCENT_CYAN),
                       label("RESILIENCIA", 28, ACCENT_MINT))
        words.arrange(RIGHT, buff=1.0).move_to(UP * 1.25)
        keys = VGroup(*[RoundedRectangle(width=0.72, height=0.48, corner_radius=0.05,
                                         color=TEXT_MUTED, stroke_width=1.5)
                        for _ in range(12)]).arrange_in_grid(rows=3, cols=4, buff=0.1)
        keys.move_to(DOWN * 0.45)
        final = label("MÉXICO   LATAM CHAMPIONSHIP", 26, ACCENT_TERRACOTTA).to_edge(DOWN, buff=0.42)
        self.play(LaggedStart(*[FadeIn(item) for item in words], lag_ratio=0.2), run_time=1.0)
        self.play(FadeIn(keys), run_time=0.8)
        self.play(FadeIn(final), run_time=0.8)
        self.wait(2.5)


class CierreEntrevistas(BaseScene):
    """Placa limpia a sustituir por los clips reales de cierre."""
    def construct(self):
        title = self.title("¿Qué consejo darías a quien empieza?")
        frame = RoundedRectangle(width=10.5, height=3.7, corner_radius=0.08,
                                 color=TEXT_MUTED, stroke_width=2.0).shift(UP * 0.1)
        text = label("INSERTAR CLIPS\nCOMPETIDORES Y ENTRENADORES", 24, TEXT_MUTED).move_to(frame)
        ages = VGroup(label("PRIMARIA", 20, ACCENT_CYAN),
                      label("SECUNDARIA", 20, ACCENT_INDIGO),
                      label("PREPARATORIA", 20, ACCENT_TERRACOTTA))
        ages.arrange(RIGHT, buff=0.85).to_edge(DOWN, buff=0.38)
        self.play(Write(title), Create(frame), FadeIn(text), run_time=1.0)
        self.play(FadeIn(ages), run_time=0.8)
        self.wait(3.0)
