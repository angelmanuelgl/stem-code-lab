"""Componentes LaTeX y geometría compartidos exclusivamente por el video 18."""
import sys
from pathlib import Path
import numpy as np
from manim import *

sys.path.append(str(Path(__file__).resolve().parents[2]))
from styles.theme import (
    BG_COLOR, TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT,
    ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN,
)

config.frame_width = 14.222
config.frame_height = 8
config.media_dir = str(Path(__file__).resolve().parent / "media")


def fit(mob, width=5.7, height=None):
    if mob.width > width:
        mob.scale_to_fit_width(width)
    if height is not None and mob.height > height:
        mob.scale_to_fit_height(height)
    return mob


def prose(value, size=30, color=TEXT_MAIN, width=5.7):
    return fit(Tex(value, font_size=size, color=color), width)


def math(value, size=36, color=TEXT_MAIN, width=5.7):
    return fit(MathTex(value, font_size=size, color=color), width)


def heading(scene, value):
    title = prose(value, 38, width=12.4).move_to(UP * 3.25)
    rule = Line(LEFT * 6.3 + UP * 2.75, RIGHT * 6.3 + UP * 2.75,
                color=TEXT_MUTED, stroke_width=1)
    scene.play(Write(title), Create(rule), run_time=1.3)
    return VGroup(title, rule)


def conclusion(scene, value):
    label = prose(value, 29, ACCENT_MINT, width=12.3).move_to(DOWN * 3.12)
    scene.play(Write(label), run_time=1.5)
    scene.wait(3)
    return label


def stack(*items, center=RIGHT * 3.1, buff=0.45):
    return VGroup(*items).arrange(DOWN, buff=buff).move_to(center)


def axes(x_range, y_range, width=5.1, height=3.7, center=LEFT * 3.15):
    return Axes(x_range=x_range, y_range=y_range, x_length=width,
                y_length=height, tips=False,
                axis_config={"color": TEXT_MUTED, "stroke_width": 1.5,
                             "include_numbers": False}).move_to(center)


def polyline(ax, xs, ys, color=ACCENT_CYAN, stroke_width=2):
    curve = VMobject(color=color, stroke_width=stroke_width)
    curve.set_points_as_corners([ax.c2p(float(x), float(y)) for x, y in zip(xs, ys)])
    return curve


def cloud(ax, points, color=ACCENT_CYAN, radius=0.012):
    return VGroup(*[Dot(ax.c2p(float(x), float(y)), radius=radius,
                       color=color, fill_opacity=0.28, stroke_width=0)
                    for x, y in points])


def correlation_points(base, rho):
    if not -1 <= rho <= 1:
        raise ValueError("rho debe pertenecer a [-1,1]")
    return np.column_stack((base[:, 0], rho * base[:, 0]
                            + np.sqrt(max(0, 1-rho*rho)) * base[:, 1]))


def covariance_ellipse(ax, rho, radius=2, color=ACCENT_MINT):
    angle = np.linspace(0, 2*np.pi, 121)
    points = correlation_points(np.column_stack((np.cos(angle), np.sin(angle))), rho)
    return polyline(ax, radius * points[:, 0], radius * points[:, 1], color)


def box(label, position, width=1.0, height=0.7, color=ACCENT_INDIGO):
    border = RoundedRectangle(width=width, height=height, corner_radius=0.1,
                              color=color, stroke_width=2).move_to(position)
    return VGroup(border, math(label, 30, width=width-0.15).move_to(position))


def arrow_between(first, second, color=ACCENT_CYAN):
    return Arrow(first.get_right(), second.get_left(), buff=0.12,
                 color=color, stroke_width=2, max_tip_length_to_length_ratio=0.15)
