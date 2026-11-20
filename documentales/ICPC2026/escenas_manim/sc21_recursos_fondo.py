"""Cierre: cuadrícula a pantalla completa con margen para bolitas y cola difuminada."""
import random
import numpy as np
from manim import *
from base_theme import BaseScene
from theme import (
    BG_COLOR,
    TEXT_MUTED,
    ACCENT_CYAN,
    ACCENT_MINT,
    ACCENT_TERRACOTTA,
    ACCENT_INDIGO,
)

MOVE_DELTAS = {
    "R": (0, 1),
    "L": (0, -1),
    "D": (1, 0),
    "U": (-1, 0),
}


def generate_varied_path(rows: int, cols: int, rng: random.Random):
    """
    Genera una ruta válida desde (0, 0) hasta (rows - 1, cols - 1) dentro de la cuadrícula,
    variando cantidad de desvíos U y L (desde 0/0 hasta varios desvíos y longitudes distintas).
    """
    goal = (rows - 1, cols - 1)
    max_extra_steps = rng.choice([0, 0, 2, 4, 6, 8, 10])
    min_required = (rows - 1) + (cols - 1)
    max_steps = min_required + max_extra_steps

    r, c = 0, 0
    coords = [(r, c)]

    for step in range(max_steps):
        if (r, c) == goal and step >= min_required and rng.random() < 0.35:
            break

        rem_steps = max_steps - step - 1
        candidates = []

        for mv, (dr, dc) in MOVE_DELTAS.items():
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            dist_after = abs(goal[0] - nr) + abs(goal[1] - nc)
            if dist_after > rem_steps:
                continue

            if len(coords) >= 2 and (nr, nc) == coords[-2]:
                continue

            candidates.append(mv)

        if not candidates:
            break

        weights = [2.2 if mv in ("R", "D") else 1.1 for mv in candidates]
        chosen = rng.choices(candidates, weights=weights, k=1)[0]
        dr, dc = MOVE_DELTAS[chosen]
        r, c = r + dr, c + dc
        coords.append((r, c))

    while (r, c) != goal:
        options = []
        if c < goal[1]:
            options.append((r, c + 1))
        if r < goal[0]:
            options.append((r + 1, c))
        if not options:
            break
        r, c = rng.choice(options)
        coords.append((r, c))

    return coords


def sample_polyline_at_distances(waypoints, seg_lengths, total_len, distances):
    """Devuelve puntos interpolados a lo largo de la polilínea para una lista de distancias."""
    if total_len <= 1e-9:
        return [waypoints[0].copy() for _ in distances]

    pts_out = []
    n_seg = len(seg_lengths)

    for d in distances:
        d_clamped = max(0.0, min(total_len, d))
        acc = 0.0
        placed = False
        for i, slen in enumerate(seg_lengths):
            if acc + slen >= d_clamped or i == n_seg - 1:
                local_t = (d_clamped - acc) / slen if slen > 1e-9 else 1.0
                local_t = max(0.0, min(1.0, local_t))
                pts_out.append(waypoints[i] + (waypoints[i + 1] - waypoints[i]) * local_t)
                placed = True
                break
            acc += slen
        if not placed:
            pts_out.append(waypoints[-1].copy())

    return pts_out


class CierrePulsosCuadricula(BaseScene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Deja un margen alrededor para que las bolitas de los bordes se vean completas
        fw = config.frame_width
        fh = config.frame_height
        margin_x = 0.24
        margin_y = 0.24
        usable_w = max(1.0, fw - 2 * margin_x)
        usable_h = max(1.0, fh - 2 * margin_y)
        is_portrait = fh > fw

        if is_portrait:
            cols = 9
            cell_size = usable_w / (cols - 1)
            rows = max(6, int(usable_h // cell_size) + 1)
        else:
            rows = 9
            cell_size = usable_h / (rows - 1)
            cols = max(8, int(usable_w // cell_size) + 1)

        grid_w = (cols - 1) * cell_size
        grid_h = (rows - 1) * cell_size
        top_left = LEFT * (grid_w / 2.0) + UP * (grid_h / 2.0)

        pts = {}
        for r in range(rows):
            for c in range(cols):
                pts[(r, c)] = top_left + RIGHT * (c * cell_size) + DOWN * (r * cell_size)

        grid_lines = VGroup()
        for r in range(rows):
            grid_lines.add(
                Line(
                    pts[(r, 0)],
                    pts[(r, cols - 1)],
                    stroke_color=TEXT_MUTED,
                    stroke_width=1.15,
                    stroke_opacity=0.16,
                )
            )
        for c in range(cols):
            grid_lines.add(
                Line(
                    pts[(0, c)],
                    pts[(rows - 1, c)],
                    stroke_color=TEXT_MUTED,
                    stroke_width=1.15,
                    stroke_opacity=0.16,
                )
            )

        grid_dots = VGroup(*[
            Dot(pt, radius=min(0.025, cell_size * 0.03), color=TEXT_MUTED, fill_opacity=0.20)
            for pt in pts.values()
        ])

        self.add(grid_lines, grid_dots)

        # Configuración del cierre: nueva bolita cada 2.0s sin esperar a las anteriores
        total_duration = 90.0
        spawn_interval = 1.5
        trail_length = cell_size * 12
        n_trail_segs = 48
        max_trail_opacity = 0.24
        dot_base_opacity = 0.60
        speed = cell_size * 1.3

        pulse_colors = [ACCENT_CYAN, ACCENT_MINT, ACCENT_INDIGO, ACCENT_TERRACOTTA]
        rng = random.Random(2026)

        active_pulses = []
        next_spawn_time = 0.0
        sim_time = 0.0
        dt = 1.0 / 60.0

        def spawn_pulse(now: float):
            coords = generate_varied_path(rows, cols, rng)
            waypoints = [pts[p] for p in coords]

            seg_lengths = [
                float(np.linalg.norm(waypoints[i + 1] - waypoints[i]))
                for i in range(len(waypoints) - 1)
            ]
            total_len = sum(seg_lengths) or 1e-6
            duration = total_len / speed

            color = rng.choice(pulse_colors)
            dot_radius = min(0.075, cell_size * 0.085)
            dot = Dot(waypoints[0], radius=dot_radius, color=color, fill_opacity=dot_base_opacity)

            base_opacities = [(1.0 - (k / n_trail_segs)) ** 1.7 for k in range(n_trail_segs)]
            trail_segs = VGroup()
            for k in range(n_trail_segs):
                seg = Line(
                    waypoints[0],
                    waypoints[0] + RIGHT * 1e-5,
                    stroke_color=color,
                    stroke_width=2.6,
                    stroke_opacity=max_trail_opacity * base_opacities[k],
                )
                trail_segs.add(seg)

            self.add(trail_segs, dot)
            active_pulses.append({
                "start": now,
                "duration": duration,
                "waypoints": waypoints,
                "seg_lengths": seg_lengths,
                "total_len": total_len,
                "base_opacities": base_opacities,
                "dot": dot,
                "trail_segs": trail_segs,
            })

        def step_pulses(dt_step):
            nonlocal sim_time, next_spawn_time
            sim_time += dt_step

            while next_spawn_time <= total_duration and sim_time >= next_spawn_time:
                spawn_pulse(next_spawn_time)
                next_spawn_time += spawn_interval

            finished = []
            for p in active_pulses:
                elapsed = sim_time - p["start"]
                if elapsed < 0:
                    continue

                alpha = elapsed / p["duration"]
                if alpha >= 1.0:
                    finished.append(p)
                    continue

                head_dist = alpha * p["total_len"]
                tail_end_fade = max(0.0, min(1.0, (1.0 - alpha) / 0.18))

                sample_dists = [
                    max(0.0, head_dist - trail_length * (k / n_trail_segs))
                    for k in range(n_trail_segs + 1)
                ]
                sampled_pts = sample_polyline_at_distances(
                    p["waypoints"],
                    p["seg_lengths"],
                    p["total_len"],
                    sample_dists,
                )

                p["dot"].move_to(sampled_pts[0])
                p["dot"].set_opacity(dot_base_opacity * min(1.0, (1.0 - alpha) / 0.08))

                for k, seg in enumerate(p["trail_segs"]):
                    p_a = sampled_pts[k]
                    p_b = sampled_pts[k + 1]
                    if np.linalg.norm(p_b - p_a) < 1e-6:
                        p_b = p_a + RIGHT * 1e-5
                    seg.put_start_and_end_on(p_a, p_b)
                    seg.set_stroke(opacity=max_trail_opacity * p["base_opacities"][k] * tail_end_fade)

            for p in finished:
                self.remove(p["dot"], p["trail_segs"])
                active_pulses.remove(p)

        elapsed_total = 0.0
        while elapsed_total < total_duration:
            chunk = min(dt, total_duration - elapsed_total)
            self.play(
                UpdateFromAlphaFunc(
                    grid_lines,
                    lambda m, alpha, d=chunk: step_pulses(d),
                    run_time=chunk,
                    rate_func=linear,
                )
            )
            elapsed_total += chunk

        for p in list(active_pulses):
            self.remove(p["dot"], p["trail_segs"])
        active_pulses.clear()