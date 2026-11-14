"""Bloque 3–4: equipo, corte de participantes y tabla final."""
from manim import *
from base_theme import BaseScene, card, label, formula
from theme import TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT, ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN


class RolesEquipo(BaseScene):
    def construct(self):
        self.play(Write(self.title("Tres funciones coordinadas")))
        roles = [
            ("ESTRATEGIA", "modelo y algoritmo", ACCENT_INDIGO),
            ("VALIDACIÓN", "casos y lógica", ACCENT_CYAN),
            ("DEPURACIÓN", "código y errores", ACCENT_TERRACOTTA),
        ]
        centers = [LEFT * 4.25, ORIGIN, RIGHT * 4.25]
        cards = VGroup()
        for (heading, detail, color), center in zip(roles, centers):
            person = VGroup(Circle(radius=0.22, color=color, stroke_width=2.5),
                            Arc(start_angle=0, angle=PI, radius=0.45, color=color, stroke_width=2.5))
            person[0].move_to(UP * 0.4)
            person[1].move_to(DOWN * 0.35)
            text = VGroup(label(heading, 22, color), label(detail, 19, TEXT_MAIN))
            text.arrange(DOWN, buff=0.2)
            group = VGroup(person, text).arrange(DOWN, buff=0.25).move_to(center + DOWN * 0.05)
            cards.add(group)
        links = VGroup(
            Arrow(cards[0].get_right(), cards[1].get_left(), color=ACCENT_MINT, buff=0.15),
            Arrow(cards[1].get_right(), cards[2].get_left(), color=ACCENT_MINT, buff=0.15),
        )
        self.play(LaggedStart(*[FadeIn(c, shift=0.12 * UP) for c in cards], lag_ratio=0.22), run_time=1.5)
        self.play(GrowArrow(links[0]), GrowArrow(links[1]), run_time=0.9)
        for index, color in enumerate((ACCENT_INDIGO, ACCENT_CYAN, ACCENT_TERRACOTTA)):
            self.play(Indicate(cards[index], color=color), run_time=0.7)
        marker = label("CLIP UADY: insertar metraje real", 19, TEXT_MUTED).to_edge(DOWN, buff=0.28)
        self.play(FadeIn(marker), run_time=0.6)
        self.wait(2.0)


class TalentoReclutadores(BaseScene):
    """Placa de inserción tipográfica para clips de reclutadores."""
    def construct(self):
        self.play(Write(self.title("Talento bajo presión")))
        frame = RoundedRectangle(width=10.7, height=4.15, corner_radius=0.08,
                                 color=TEXT_MUTED, stroke_width=2.0)
        caption = label("INSERTAR CLIP DE RECLUTADORES", 24, TEXT_MUTED, width=9.6).move_to(frame)
        frame.shift(UP * 0.15)
        caption.move_to(frame)
        self.play(Create(frame), FadeIn(caption), run_time=1.0)
        tags = VGroup(label("ANÁLISIS", 21, ACCENT_INDIGO),
                      label("RESILIENCIA", 21, ACCENT_MINT),
                      label("COLABORACIÓN", 21, ACCENT_CYAN))
        tags.arrange(RIGHT, buff=0.75).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(tags), run_time=0.8)
        for tag in tags:
            self.play(Indicate(tag), run_time=0.75)
        self.wait(1.8)


class EntradaResultados(BaseScene):
    def construct(self):
        self.play(Write(self.title("Final Mexicana 2026")))
        board = RoundedRectangle(width=10.8, height=4.25, corner_radius=0.08,
                                 color=ACCENT_CYAN, stroke_width=2.2)
        lines = VGroup(*[Line(LEFT * 4.8, RIGHT * 4.8, color=TEXT_MUTED, stroke_width=1.2)
                         for _ in range(2)]).arrange(DOWN, buff=1.15).move_to(DOWN * 0.1)
        self.play(Create(board), Create(lines), run_time=1.2)
        self.wait(2.2)


class FiltroEquipos(BaseScene):
    def construct(self):
        self.play(Write(self.title("Tres filtros, tres cantidades")))
        data = [("509", "clasificatorias", ACCENT_CYAN),
                ("85", "final presencial", ACCENT_INDIGO),
                ("20", "medallistas", ACCENT_MINT)]
        groups = VGroup()
        xs = [-4.35, 0, 4.35]
        for (number, caption, color), x in zip(data, xs):
            circle = Circle(radius=0.92, color=color, stroke_width=2.8)
            value = formula(number, 39, color).move_to(circle)
            note = label(caption, 21, TEXT_MAIN, width=3.2).next_to(circle, DOWN, buff=0.32)
            groups.add(VGroup(circle, value, note).move_to(x * RIGHT + DOWN * 0.15))
        arrows = VGroup(*[
            Arrow(groups[i].get_right(), groups[i + 1].get_left(), color=TEXT_MUTED,
                  stroke_width=2.0, buff=0.18)
            for i in range(2)
        ])
        self.play(FadeIn(groups[0]), run_time=0.8)
        self.wait(0.6)
        self.play(GrowArrow(arrows[0]), FadeIn(groups[1]), run_time=1.0)
        self.wait(0.6)
        self.play(GrowArrow(arrows[1]), FadeIn(groups[2]), run_time=1.0)
        self.wait(2.0)


class MedallasPorRendimiento(BaseScene):
    def construct(self):
        self.play(Write(self.title("La tabla reconoce bloques de rendimiento")))
        one = VGroup(Circle(radius=0.66, color=ACCENT_TERRACOTTA, stroke_width=2.6),
                     label("1\nCAMPEÓN", 20, TEXT_MAIN))
        one[1].move_to(one[0]).shift(DOWN * 0.08)
        one.move_to(LEFT * 4.2 + DOWN * 0.05)
        bands = VGroup()
        for name, color in (("ORO", ACCENT_TERRACOTTA), ("PLATA", ACCENT_CYAN), ("BRONCE", ACCENT_VINO)):
            frame = RoundedRectangle(width=5.3, height=0.78, corner_radius=0.08,
                                     color=color, stroke_width=2.4)
            tag = label(name, 22, color).move_to(frame)
            bands.add(VGroup(frame, tag))
        bands.arrange(DOWN, buff=0.22).move_to(RIGHT * 1.6 + UP * 0.1)
        arrow = Arrow(one.get_right(), bands.get_left(), color=TEXT_MUTED, buff=0.18)
        note = label("estándar global de rendimiento\n+ porcentajes de participación", 21,
                     TEXT_MUTED).move_to(RIGHT * 1.6 + DOWN * 2.25)
        self.play(FadeIn(one), GrowArrow(arrow), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(band) for band in bands], lag_ratio=0.24), run_time=1.3)
        self.play(FadeIn(note), run_time=0.7)
        self.wait(2.1)


# Datos fuente del guion. Las abreviaciones se aplican solo a la etiqueta visible.
TOP25 = [
    (1, "ESCOM IPN", 'Domain Expansion "Abraham échate un hint"', 10, "Sí clasificó"),
    (2, "CCM", "Chatcito, Claudecito y Geminicito - Campeones OMI 2026", 10, "No [Invitado / Guest]"),
    (3, "U de Guanajuato", "Soy malo y eso es bueno, yo jamás seré bueno y eso no es malo", 9, "Sí clasificó"),
    (4, "UP GDL", "Prisioneros de Alcatraz", 8, "Sí clasificó"),
    (5, "ITESM Monterrey", "Academia de Pilotaje Aerostático Manuel Doblado (Clases Privadas...)", 8, "Sí clasificó"),
    (6, "UP Bonaterra", "The good, the bad and the ugly", 8, "Sí clasificó"),
    (7, "FC-UNAM", "Oasis", 8, "Sí clasificó"),
    (8, "U de Guanajuato", "ICAxiom", 8, "Sí clasificó"),
    (9, "IT Culiacán", "Los guerreros más fuertes de wkoder", 8, "Sí clasificó"),
    (10, "UADY", "Gauss N' Roses", 8, "Sí clasificó"),
    (11, "UANL", "No te preocupes, mención honorífica también es buen resultado", 8, "Sí clasificó"),
    (12, "UADY", "PEScapitalista", 8, "Sí clasificó"),
    (13, "Facultad de Ingeniería UNAM", ":)", 8, "Sí clasificó"),
    (14, "UdG CUCEI", "Adrián quería que nos pusiéramos un nombre largo...", 8, "Sí clasificó"),
    (15, "ITESM GDA", "Hijos del Puntero", 7, "No"),
    (16, "UADY", "Tuntunsitos", 7, "No"),
    (17, "ESCOM IPN", "Las Chivas de Milito", 7, "No"),
    (18, "IT Culiacán", "AD-HOCK", 7, "No"),
    (19, "U de Guanajuato", "Mäthgic Crüe", 7, "No"),
    (20, "FC-UNAM", "Claude Opus 4.6", 7, "No"),
    (21, "ITESM Monterrey", "Data Divas", 6, "Sí clasificó"),
    (22, "ITESM Monterrey", "ATCSUSMS (Alianza)", 6, "Sí clasificó"),
    (23, "UAM A", "Seal++", 6, "Sí clasificó"),
    (24, "UASLP", "Tacos de Schnauzer", 6, "Sí clasificó"),
    (25, "UAEH", "CapyBaby's", 6, "Sí clasificó"),
]


def _shorten(text, limit=45):
    return text if len(text) <= limit else text[:limit - 1].rstrip() + "..."


class TablaTop25(BaseScene):
    def construct(self):
        self._page(0, 14, "Final Mexicana - equipos 1–14")
        self.wait(1.1)
        self.clear_scene()
        self._page(14, 25, "Final Mexicana - equipos 15–25")
        self.wait(2.0)

    def _page(self, begin, end, heading):
        title = self.title(heading)
        widths = [0.65, 2.1, 5.4, 1.1, 2.2]
        left = -6.1
        xs = [left + sum(widths[:i]) + widths[i] / 2 for i in range(len(widths))]
        header_y = 2.55
        headers = ["#", "Institución", "Equipo", "Problemas", "Estatus"]
        header_objs = VGroup()
        for i, (txt, width) in enumerate(zip(headers, widths)):
            header_objs.add(label(txt, 18, ACCENT_CYAN, width - 0.08).move_to([xs[i], header_y, 0]))
        rule = Line(LEFT * 6.35 + UP * 2.28, RIGHT * 6.35 + UP * 2.28,
                    color=ACCENT_CYAN, stroke_width=1.8)
        self.play(FadeIn(title), FadeIn(header_objs), Create(rule), run_time=0.9)
        entries = TOP25[begin:end]
        row_step = 4.55 / len(entries)
        rows = VGroup()
        for index, (rank, school, team, solved, status) in enumerate(entries):
            y = 2.03 - index * row_step
            vals = [str(rank), school, _shorten(team, 58), str(solved), status]
            for col, (value, width) in enumerate(zip(vals, widths)):
                color = ACCENT_MINT if col == 4 and status.startswith("Sí") else (
                    ACCENT_VINO if col == 4 else TEXT_MAIN)
                obj = label(value, 17, color, width - 0.12).move_to([xs[col], y, 0])
                rows.add(obj)
        self.play(LaggedStart(*[FadeIn(row) for row in rows], lag_ratio=0.02), run_time=1.4)
        self.wait(2.8)
