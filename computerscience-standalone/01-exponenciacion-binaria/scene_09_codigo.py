from manim import *
import numpy as np
from scene_utils import *


class Escena09Codigo(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG_COLOR
        self.add(heading(9, "Del dibujo al código"))
        source = ["long long binpow(long long a,", "                 long long b, long long m) {", "    long long res = 1;", "    a %= m;", "    while (b > 0) {", "        if (b & 1) res = (res * a) % m;", "        a = (a * a) % m;", "        b >>= 1;", "    }", "    return res;", "}"]
        # LaTeX typewriter face; escaping keeps %, &, braces and >> literal.
        lines = VGroup(*[Tex(r"\ttfamily " + escape_tex(line.lstrip()), font_size=26, color=TEXT_MAIN) for line in source]).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        # Preserve indentation: arrange aligns glyph bounds, so restore source indent.
        for line, text in zip(lines, source):
            line.shift(RIGHT * (len(text) - len(text.lstrip())) * 0.102)
        if lines.width > 6:
            lines.scale_to_fit_width(6)
        lines.move_to(LEFT * 3.1 + DOWN * 0.25)
        panel = SurroundingRectangle(lines, color=TEXT_MUTED, fill_color=PANEL_COLOR, fill_opacity=1, buff=0.25)
        # [TRIGGER_1] Código para a,b >= 0 y m = 10^9+7.
        self.play(FadeIn(panel), FadeIn(lines))
        # [TRIGGER_2] Recorrer todos los bits.
        highlight = SurroundingRectangle(lines[4], color=COLOR_MODULO, buff=0.06)
        self.play(Create(highlight))
        self.wait(1)
        # [TRIGGER_3] Comprobar el bit menos significativo.
        self.play(Transform(highlight, SurroundingRectangle(lines[5], color=COLOR_OPTIMAL, buff=0.06)))
        self.wait(1)
        # [TRIGGER_4] Cuadrado y desplazamiento.
        self.play(Transform(highlight, SurroundingRectangle(VGroup(lines[6], lines[7]), color=COLOR_EXPOS, buff=0.06)))
        self.wait(1)
        # [TRIGGER_5] Ambas curvas usan la misma escala.
        axes = Axes(x_range=[0, 32, 8], y_range=[0, 32, 8], x_length=4.6, y_length=3.5, axis_config={"color": TEXT_MUTED, "include_tip": False}).move_to(RIGHT * 3.7 + DOWN * 0.1)
        linear = axes.plot(lambda x: x, x_range=[1, 32], color=COLOR_FORCE_BRUTE)
        logarithmic = axes.plot(lambda x: np.log2(x), x_range=[1, 32], color=COLOR_OPTIMAL)
        legend = VGroup(formula("n", 29, COLOR_FORCE_BRUTE), formula(r"\log_2 n", 29, COLOR_OPTIMAL)).arrange(RIGHT, buff=0.8).move_to(RIGHT * 3.7 + UP * 2.1)
        self.play(Create(axes), FadeIn(legend))
        self.play(Create(linear), Create(logarithmic), run_time=2)
        count = formula(r"\lfloor\log_2 n\rfloor+1\;\text{bits}\quad(n>0)", 26).move_to(RIGHT * 3.6 + DOWN * 2.5)
        self.play(Write(count))
        self.play(FadeIn(label("Módulo fijo: O(log n) operaciones aritméticas", 24, COLOR_OPTIMAL).to_edge(DOWN, buff=0.35)))
        self.wait(3)
