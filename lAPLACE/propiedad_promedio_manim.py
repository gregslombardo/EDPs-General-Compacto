from __future__ import annotations

import os
import tempfile
from pathlib import Path

import numpy as np
from manim import *

# ============================================================
# CONFIGURACIÓN GLOBAL: 2K, 120 FPS, render local de alta calidad
# ============================================================

config.pixel_width = 2560
config.pixel_height = 1440
config.frame_rate = 120
config.background_color = "#0f1115"
config.media_dir = str(Path.cwd() / "media_propiedad_promedio")

# Robustez para Windows / MiKTeX.
try:
    config.no_latex_cleanup = True
except Exception:
    pass

try:
    tex_dir = Path(tempfile.gettempdir()) / f"manim_tex_promedio_{os.getpid()}"
    tex_dir.mkdir(parents=True, exist_ok=True)
    config.tex_dir = str(tex_dir)
except Exception:
    pass

# ============================================================
# DATOS MATEMÁTICOS
# ============================================================

A = np.array([0.75, 0.35])
CENTER_SHIFT = np.array([-3.6, -0.15, 0.0])

def u_harmonic(x: float, y: float) -> float:
    """Función armónica: Δu = 0."""
    return x**2 - y**2 + 0.6*x - 0.4*y + 1.2

def v_nonharmonic(x: float, y: float) -> float:
    """Función no armónica: Δv = 4."""
    return x**2 + y**2 + 0.25*x - 0.15*y + 0.8

U0 = u_harmonic(A[0], A[1])
V0 = v_nonharmonic(A[0], A[1])

def boundary_mean_u(r: float) -> float:
    # Para una función armónica, el promedio sobre toda circunferencia es u(A).
    return U0

def boundary_mean_v(r: float) -> float:
    # Para v=x^2+y^2+afín+cte, el promedio sobre ∂B_r(A) es v(A)+r^2.
    return V0 + r**2

def disk_mean_v(r: float) -> float:
    # En dimensión 2, el promedio de |x-A|^2 sobre B_r(A) es r^2/2.
    return V0 + 0.5*r**2

def value_color(value: float, lo: float = -2.0, hi: float = 6.0):
    alpha = np.clip((value - lo) / (hi - lo), 0.0, 1.0)
    return interpolate_color(BLUE_E, RED_E, alpha)

def make_panel(width=6.0, height=5.5):
    panel = RoundedRectangle(
        corner_radius=0.18,
        width=width,
        height=height,
        stroke_width=1.5,
        stroke_color=GRAY_B,
        fill_color=BLACK,
        fill_opacity=0.22,
    )
    return panel

def format_decimal(number: float, places: int = 6):
    return DecimalNumber(
        number,
        num_decimal_places=places,
        include_sign=False,
        font_size=34,
    )


def safe_title(text: str, font_size: int = 44):
    """Título centrado con margen lateral garantizado en cualquier render."""
    title = Text(text, font_size=font_size, weight=BOLD)
    max_width = config.frame_width - 1.4
    if title.width > max_width:
        title.scale_to_fit_width(max_width)
    return title.to_edge(UP, buff=0.32)

# ============================================================
# ESCENA 1
# ============================================================

class PromedioCircunferencia(Scene):
    """
    Visualiza:
        u(A) = (1 / |∂B_r|) ∫_{∂B_r(A)} u dS
    para una función armónica u.
    """

    def construct(self):
        title = safe_title("Propiedad del promedio sobre circunferencias")

        subtitle = MathTex(
            r"\Delta u=0",
            r"\quad\Longrightarrow\quad",
            r"u(a)=\frac{1}{2\pi r}\int_{\partial B_r(a)}u\,ds",
            font_size=39,
        ).next_to(title, DOWN, buff=0.22)

        # Cartela inicial legible desde el primer fotograma.
        self.add(title, subtitle)
        self.wait(4.0)

        plane = NumberPlane(
            x_range=[-2.5, 3.0, 1.0],
            y_range=[-2.5, 2.8, 1.0],
            x_length=6.3,
            y_length=6.1,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_opacity": 0.25,
                "stroke_width": 1,
            },
            axis_config={"stroke_color": GRAY_B, "stroke_width": 1.5},
        ).shift(CENTER_SHIFT)

        panel = make_panel(6.4, 6.1).move_to([3.55, -0.15, 0.0])

        r = ValueTracker(0.65)
        theta = ValueTracker(0.02)

        center_point = plane.c2p(A[0], A[1])
        center_dot = Dot(center_point, radius=0.09, color=YELLOW)
        center_label = MathTex("a", font_size=34).next_to(center_dot, UR, buff=0.1)

        circle = always_redraw(
            lambda: Circle(
                radius=plane.x_axis.get_unit_size() * r.get_value(),
                color=YELLOW,
                stroke_width=5,
            ).move_to(center_point)
        )

        def boundary_dots():
            rr = r.get_value()
            dots = VGroup()
            for k in range(72):
                ang = TAU * k / 72
                x = A[0] + rr * np.cos(ang)
                y = A[1] + rr * np.sin(ang)
                d = Dot(
                    plane.c2p(x, y),
                    radius=0.037,
                    color=value_color(u_harmonic(x, y)),
                )
                dots.add(d)
            return dots

        dots = always_redraw(boundary_dots)

        moving_dot = always_redraw(
            lambda: Dot(
                plane.c2p(
                    A[0] + r.get_value() * np.cos(theta.get_value()),
                    A[1] + r.get_value() * np.sin(theta.get_value()),
                ),
                radius=0.085,
                color=WHITE,
            )
        )

        radius_segment = always_redraw(
            lambda: Line(
                center_point,
                plane.c2p(
                    A[0] + r.get_value() * np.cos(theta.get_value()),
                    A[1] + r.get_value() * np.sin(theta.get_value()),
                ),
                color=WHITE,
                stroke_width=2.5,
            )
        )

        self.play(
            Create(plane),
            FadeIn(panel),
            FadeIn(center_dot),
            Write(center_label),
            Create(circle),
            FadeIn(dots),
            run_time=4.0,
        )
        self.wait(2.0)

        func = MathTex(
            r"u(x,y)=x^2-y^2+0.6x-0.4y+1.2",
            font_size=34,
        ).move_to([3.55, 2.1, 0.0])

        lap = MathTex(
            r"\Delta u=u_{xx}+u_{yy}=2-2=0",
            font_size=34,
        ).next_to(func, DOWN, buff=0.35)

        r_label = MathTex("r=", font_size=34).move_to([1.65, 0.95, 0.0])
        r_value = always_redraw(
            lambda: DecimalNumber(
                r.get_value(),
                num_decimal_places=3,
                font_size=34,
            ).next_to(r_label, RIGHT, buff=0.15)
        )

        center_text = MathTex(r"u(a)=", font_size=34).move_to([1.9, 0.25, 0.0])
        center_value = format_decimal(U0).next_to(center_text, RIGHT, buff=0.15)

        mean_text = MathTex(
            r"\frac{1}{2\pi r}\int_{\partial B_r(a)}u\,ds=",
            font_size=31,
        ).move_to([2.35, -0.55, 0.0])

        mean_value = always_redraw(
            lambda: DecimalNumber(
                boundary_mean_u(r.get_value()),
                num_decimal_places=6,
                font_size=34,
                color=GREEN_C,
            ).next_to(mean_text, RIGHT, buff=0.15)
        )

        error_text = MathTex(r"\mathrm{error}=", font_size=34).move_to([1.95, -1.35, 0.0])
        error_value = always_redraw(
            lambda: DecimalNumber(
                abs(boundary_mean_u(r.get_value()) - U0),
                num_decimal_places=8,
                font_size=34,
                color=GREEN_C,
            ).next_to(error_text, RIGHT, buff=0.15)
        )

        explanation = Text(
            "El radio cambia, pero el promedio permanece fijo.",
            font_size=29,
        ).move_to([3.55, -2.2, 0.0])

        self.play(
            Write(func),
            Write(lap),
            Write(r_label),
            FadeIn(r_value),
            Write(center_text),
            FadeIn(center_value),
            Write(mean_text),
            FadeIn(mean_value),
            Write(error_text),
            FadeIn(error_value),
            FadeIn(explanation),
            run_time=4.5,
        )
        self.wait(3.0)

        # Variación lenta del radio: larga duración.
        self.play(r.animate.set_value(2.0), run_time=12.0, rate_func=smooth)
        self.wait(2.0)
        self.play(r.animate.set_value(1.15), run_time=8.0, rate_func=smooth)
        self.wait(2.0)

        self.play(FadeIn(radius_segment), FadeIn(moving_dot), run_time=1.5)
        self.play(theta.animate.set_value(TAU + 0.02), run_time=14.0, rate_func=linear)
        self.wait(3.0)

        box = SurroundingRectangle(
            VGroup(center_text, center_value, mean_text, mean_value),
            color=GREEN_C,
            buff=0.2,
        )
        conclusion = Text(
            "El valor en el centro coincide con el promedio de la frontera.",
            font_size=31,
            weight=BOLD,
        ).to_edge(DOWN)

        self.play(Create(box), FadeIn(conclusion, shift=UP), run_time=2.5)
        self.wait(5.0)


# ============================================================
# ESCENA 2
# ============================================================

class PromedioDisco(Scene):
    """
    Visualiza:
        u(A) = (1 / |B_r|) ∫_{B_r(A)} u(x) dx
    usando una cuadratura simétrica por anillos.
    """

    def construct(self):
        title = safe_title("Propiedad del promedio sobre discos")

        formula = MathTex(
            r"u(a)=\frac{1}{\pi r^2}\int_{B_r(a)}u(x,y)\,dx\,dy",
            font_size=40,
        ).next_to(title, DOWN, buff=0.22)

        # Cartela inicial legible desde el primer fotograma.
        self.add(title, formula)
        self.wait(4.0)

        plane = NumberPlane(
            x_range=[-2.5, 3.0, 1.0],
            y_range=[-2.5, 2.8, 1.0],
            x_length=6.3,
            y_length=6.1,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_opacity": 0.25,
                "stroke_width": 1,
            },
            axis_config={"stroke_color": GRAY_B, "stroke_width": 1.5},
        ).shift(CENTER_SHIFT)

        panel = make_panel(6.4, 6.1).move_to([3.55, -0.15, 0.0])
        center_point = plane.c2p(A[0], A[1])
        center_dot = Dot(center_point, radius=0.09, color=YELLOW)
        center_label = MathTex("a", font_size=34).next_to(center_dot, UR, buff=0.1)

        R = 1.9
        disk = Circle(
            radius=plane.x_axis.get_unit_size() * R,
            color=YELLOW,
            fill_color=YELLOW_E,
            fill_opacity=0.07,
            stroke_width=5,
        ).move_to(center_point)

        # Puntos distribuidos por anillos; cada anillo usa ángulos simétricos.
        rings = VGroup()
        ring_groups = []
        n_rings = 10
        for j in range(1, n_rings + 1):
            rho = R * np.sqrt(j / n_rings)
            group = VGroup()
            n_theta = 32
            for k in range(n_theta):
                ang = TAU * k / n_theta
                x = A[0] + rho * np.cos(ang)
                y = A[1] + rho * np.sin(ang)
                group.add(
                    Dot(
                        plane.c2p(x, y),
                        radius=0.036,
                        color=value_color(u_harmonic(x, y)),
                    )
                )
            ring_groups.append(group)
            rings.add(group)

        self.play(
            Create(plane),
            FadeIn(panel),
            FadeIn(center_dot),
            Write(center_label),
            Create(disk),
            run_time=4.0,
        )
        self.wait(2.0)

        func = MathTex(
            r"u(x,y)=x^2-y^2+0.6x-0.4y+1.2",
            font_size=34,
        ).move_to([3.55, 2.05, 0.0])

        center_text = MathTex(r"u(a)=", font_size=34).move_to([1.95, 0.95, 0.0])
        center_value = format_decimal(U0).next_to(center_text, RIGHT, buff=0.15)

        approx_text = MathTex(
            r"\mathrm{promedio\ discreto}=",
            font_size=31,
        ).move_to([2.25, 0.05, 0.0])

        approx_value = DecimalNumber(
            0.0,
            num_decimal_places=6,
            font_size=34,
            color=GREEN_C,
        ).next_to(approx_text, RIGHT, buff=0.15)

        count_text = Text("Anillos incluidos:", font_size=30).move_to([2.15, -0.8, 0.0])
        count_value = Integer(0, font_size=34).next_to(count_text, RIGHT, buff=0.18)

        note = Text(
            "La simetría angular cancela los términos no constantes.",
            font_size=28,
        ).move_to([3.55, -1.7, 0.0])

        self.play(
            Write(func),
            Write(center_text),
            FadeIn(center_value),
            Write(approx_text),
            FadeIn(approx_value),
            FadeIn(count_text),
            FadeIn(count_value),
            FadeIn(note),
            run_time=4.0,
        )
        self.wait(3.0)

        collected_values = []
        for j, group in enumerate(ring_groups, start=1):
            rho = R * np.sqrt(j / n_rings)
            for k in range(32):
                ang = TAU * k / 32
                x = A[0] + rho * np.cos(ang)
                y = A[1] + rho * np.sin(ang)
                collected_values.append(u_harmonic(x, y))

            avg = float(np.mean(collected_values))
            self.play(
                LaggedStart(*[FadeIn(dot, scale=0.4) for dot in group], lag_ratio=0.02),
                ChangeDecimalToValue(approx_value, avg),
                count_value.animate.set_value(j),
                run_time=2.3,
            )
            self.wait(0.65)

        # Añadimos el punto central con un peso visual para completar la intuición.
        pulse = Circle(radius=0.24, color=GREEN_C, stroke_width=5).move_to(center_point)
        self.play(Create(pulse), run_time=1.0)
        self.play(pulse.animate.scale(1.8).set_opacity(0), run_time=1.3)

        equality = MathTex(
            r"\frac{1}{|B_r|}\int_{B_r(a)}u=u(a)",
            font_size=42,
            color=GREEN_C,
        ).move_to([3.55, -2.45, 0.0])

        self.play(Write(equality), run_time=2.5)
        self.wait(6.0)


# ============================================================
# ESCENA 3
# ============================================================

class ComparacionArmonicaNoArmonica(Scene):
    """
    Compara una función armónica con una función no armónica.
    Para la segunda, el promedio de frontera cambia con r.
    """

    def construct(self):
        title = safe_title("La hipótesis de harmonicidad es esencial")

        self.add(title)
        self.wait(4.0)

        left_panel = make_panel(6.2, 6.2).move_to([-3.35, -0.2, 0.0])
        right_panel = make_panel(6.2, 6.2).move_to([3.35, -0.2, 0.0])
        divider = Line([0, 2.8, 0], [0, -3.2, 0], color=GRAY_B, stroke_width=2)

        self.play(FadeIn(left_panel), FadeIn(right_panel), Create(divider), run_time=2.0)

        left_title = Text("Armónica", font_size=38, weight=BOLD, color=GREEN_C).move_to([-3.35, 2.45, 0])
        right_title = Text("No armónica", font_size=38, weight=BOLD, color=RED_C).move_to([3.35, 2.45, 0])

        left_func = MathTex(
            r"u=x^2-y^2+0.6x-0.4y+1.2",
            font_size=30,
        ).move_to([-3.35, 1.85, 0])

        right_func = MathTex(
            r"v=x^2+y^2+0.25x-0.15y+0.8",
            font_size=30,
        ).move_to([3.35, 1.85, 0])

        left_lap = MathTex(r"\Delta u=0", font_size=38, color=GREEN_C).move_to([-3.35, 1.25, 0])
        right_lap = MathTex(r"\Delta v=4", font_size=38, color=RED_C).move_to([3.35, 1.25, 0])

        self.play(
            FadeIn(left_title),
            FadeIn(right_title),
            Write(left_func),
            Write(right_func),
            Write(left_lap),
            Write(right_lap),
            run_time=3.5,
        )
        self.wait(2.0)

        r = ValueTracker(0.25)

        left_center = np.array([-3.35, -0.55, 0.0])
        right_center = np.array([3.35, -0.55, 0.0])
        unit = 1.15

        left_circle = always_redraw(
            lambda: Circle(
                radius=unit * r.get_value(),
                color=YELLOW,
                stroke_width=5,
            ).move_to(left_center)
        )
        right_circle = always_redraw(
            lambda: Circle(
                radius=unit * r.get_value(),
                color=YELLOW,
                stroke_width=5,
            ).move_to(right_center)
        )

        left_dot = Dot(left_center, radius=0.09, color=WHITE)
        right_dot = Dot(right_center, radius=0.09, color=WHITE)

        self.play(
            FadeIn(left_dot),
            FadeIn(right_dot),
            Create(left_circle),
            Create(right_circle),
            run_time=2.0,
        )

        r_text = MathTex("r=", font_size=32).move_to([0.0, -0.25, 0.0])
        r_value = always_redraw(
            lambda: DecimalNumber(
                r.get_value(),
                num_decimal_places=3,
                font_size=32,
            ).next_to(r_text, RIGHT, buff=0.12)
        )

        left_center_text = MathTex(r"u(a)=", font_size=31).move_to([-4.45, -2.1, 0.0])
        left_center_value = format_decimal(U0, 5).next_to(left_center_text, RIGHT, buff=0.12)

        left_mean_text = MathTex(r"\mathrm{prom}_{\partial B_r}u=", font_size=30).move_to([-4.0, -2.65, 0.0])
        left_mean_value = always_redraw(
            lambda: DecimalNumber(
                boundary_mean_u(r.get_value()),
                num_decimal_places=5,
                font_size=31,
                color=GREEN_C,
            ).next_to(left_mean_text, RIGHT, buff=0.12)
        )

        right_center_text = MathTex(r"v(a)=", font_size=31).move_to([2.2, -2.1, 0.0])
        right_center_value = format_decimal(V0, 5).next_to(right_center_text, RIGHT, buff=0.12)

        right_mean_text = MathTex(r"\mathrm{prom}_{\partial B_r}v=", font_size=30).move_to([2.65, -2.65, 0.0])
        right_mean_value = always_redraw(
            lambda: DecimalNumber(
                boundary_mean_v(r.get_value()),
                num_decimal_places=5,
                font_size=31,
                color=RED_C,
            ).next_to(right_mean_text, RIGHT, buff=0.12)
        )

        self.play(
            Write(r_text),
            FadeIn(r_value),
            Write(left_center_text),
            FadeIn(left_center_value),
            Write(left_mean_text),
            FadeIn(left_mean_value),
            Write(right_center_text),
            FadeIn(right_center_value),
            Write(right_mean_text),
            FadeIn(right_mean_value),
            run_time=3.5,
        )
        self.wait(2.0)

        self.play(r.animate.set_value(1.75), run_time=14.0, rate_func=smooth)
        self.wait(3.0)
        self.play(r.animate.set_value(0.55), run_time=9.0, rate_func=smooth)
        self.wait(2.0)
        self.play(r.animate.set_value(1.35), run_time=8.0, rate_func=smooth)
        self.wait(3.0)

        left_result = MathTex(
            r"\mathrm{prom}_{\partial B_r}u=u(a)",
            font_size=34,
            color=GREEN_C,
        ).move_to([-3.35, -3.0, 0.0])

        right_result = MathTex(
            r"\mathrm{prom}_{\partial B_r}v=v(a)+r^2",
            font_size=34,
            color=RED_C,
        ).move_to([3.35, -3.0, 0.0])

        self.play(Write(left_result), Write(right_result), run_time=3.0)
        self.wait(5.0)


# ============================================================
# ESCENA 4: RESUMEN COMPLETO
# ============================================================

class ResumenPropiedadPromedio(Scene):
    def construct(self):
        title = safe_title("Propiedad del promedio para funciones armónicas")

        hypotheses = VGroup(
            MathTex(r"\Omega\subset\mathbb{R}^n\ \mathrm{abierto}", font_size=36),
            MathTex(r"u\in C^2(\Omega),\qquad \Delta u=0", font_size=36),
            MathTex(r"\overline{B_r(x_0)}\subset\Omega", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).shift(UP * 0.9)

        sphere = MathTex(
            r"u(x_0)=\frac{1}{|\partial B_r(x_0)|}"
            r"\int_{\partial B_r(x_0)}u\,dS",
            font_size=43,
            color=YELLOW,
        ).shift(DOWN * 0.65)

        ball = MathTex(
            r"u(x_0)=\frac{1}{|B_r(x_0)|}"
            r"\int_{B_r(x_0)}u(x)\,dx",
            font_size=43,
            color=GREEN_C,
        ).shift(DOWN * 1.75)

        note = Text(
            "Ambas identidades valen para todo radio admisible.",
            font_size=30,
        ).to_edge(DOWN)

        self.add(title)
        self.wait(4.0)
        self.play(LaggedStart(*[Write(m) for m in hypotheses], lag_ratio=0.25), run_time=4.0)
        self.wait(2.0)
        self.play(Write(sphere), run_time=3.0)
        self.wait(2.0)
        self.play(Write(ball), run_time=3.0)
        self.wait(2.0)
        self.play(FadeIn(note, shift=UP), run_time=2.0)
        self.wait(7.0)
