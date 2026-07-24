from manim import *
import numpy as np


class HeatKernelEvolution(Scene):
    def construct(self):
        self.camera.background_color = "#08111f"

        # ------------------------------------------------------------
        # Datos matemáticos
        # ------------------------------------------------------------
        t_initial = 0.08
        t_final = 2.00
        tracker = ValueTracker(t_initial)

        def heat_kernel(x, t):
            return np.exp(-(x**2) / (4.0 * t)) / np.sqrt(4.0 * np.pi * t)

        # ------------------------------------------------------------
        # Título y fórmula
        # ------------------------------------------------------------
        title = Text(
            "Evolución del núcleo fundamental del calor",
            font_size=38,
            weight=BOLD,
            color=WHITE,
        ).to_edge(UP, buff=0.22)

        formula = MathTex(
            r"\Phi(x,t)=",
            r"\frac{1}{\sqrt{4\pi t}}",
            r"\exp\left(-\frac{x^2}{4t}\right)",
            font_size=38,
        )
        formula.next_to(title, DOWN, buff=0.15)
        formula[1].set_color(YELLOW)
        formula[2].set_color(BLUE_B)

        # ------------------------------------------------------------
        # Sistema de coordenadas
        # ------------------------------------------------------------
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 1.1, 0.2],
            x_length=9.2,
            y_length=4.8,
            tips=False,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 24,
            },
            x_axis_config={
                "numbers_to_include": [-4, -2, 0, 2, 4],
            },
            y_axis_config={
                "numbers_to_include": [0.2, 0.4, 0.6, 0.8, 1.0],
            },
        )
        axes.shift(LEFT * 1.55 + DOWN * 0.75)

        axis_labels = axes.get_axis_labels(
            MathTex("x", font_size=32),
            MathTex(r"\Phi(x,t)", font_size=30),
        )

        # ------------------------------------------------------------
        # Curva y área dinámica
        # ------------------------------------------------------------
        def kernel_curve():
            t = tracker.get_value()
            xs = np.linspace(-5.0, 5.0, 500)
            points = [
                axes.c2p(x, heat_kernel(x, t))
                for x in xs
            ]

            curve = VMobject()
            curve.set_points_as_corners(points)
            curve.set_stroke(BLUE_A, width=5)
            return curve

        def kernel_area():
            t = tracker.get_value()
            xs = np.linspace(-5.0, 5.0, 350)

            points = [axes.c2p(-5.0, 0.0)]
            points.extend(
                axes.c2p(x, heat_kernel(x, t))
                for x in xs
            )
            points.append(axes.c2p(5.0, 0.0))

            area = Polygon(
                *points,
                stroke_width=0,
                fill_color=BLUE_D,
                fill_opacity=0.32,
            )
            return area

        area = always_redraw(kernel_area)
        curve = always_redraw(kernel_curve)

        maximum_point = always_redraw(
            lambda: Dot(
                axes.c2p(
                    0.0,
                    heat_kernel(0.0, tracker.get_value()),
                ),
                radius=0.065,
                color=YELLOW,
            )
        )

        # ------------------------------------------------------------
        # Panel de información
        # ------------------------------------------------------------
        panel = RoundedRectangle(
            width=3.35,
            height=3.75,
            corner_radius=0.16,
            stroke_color=GREY_B,
            stroke_width=1.5,
            fill_color="#111d30",
            fill_opacity=0.94,
        )
        panel.shift(RIGHT * 4.75 + DOWN * 0.65)

        panel_title = Text(
            "Propiedades",
            font_size=29,
            weight=BOLD,
            color=WHITE,
        )
        panel_title.move_to(panel.get_top() + DOWN * 0.35)

        t_label = MathTex("t=", font_size=31, color=YELLOW)
        t_number = DecimalNumber(
            t_initial,
            num_decimal_places=3,
            font_size=31,
            color=YELLOW,
        )
        t_number.add_updater(
            lambda mob: mob.set_value(tracker.get_value())
        )
        t_row = VGroup(t_label, t_number).arrange(RIGHT, buff=0.12)

        peak_label = MathTex(
            r"\max_x\Phi=",
            font_size=27,
            color=BLUE_A,
        )
        peak_number = DecimalNumber(
            heat_kernel(0.0, t_initial),
            num_decimal_places=4,
            font_size=27,
            color=BLUE_A,
        )
        peak_number.add_updater(
            lambda mob: mob.set_value(
                heat_kernel(0.0, tracker.get_value())
            )
        )
        peak_row = VGroup(
            peak_label,
            peak_number,
        ).arrange(RIGHT, buff=0.10)

        variance_label = MathTex(
            r"\operatorname{Var}=2t=",
            font_size=27,
            color=GREEN_A,
        )
        variance_number = DecimalNumber(
            2.0 * t_initial,
            num_decimal_places=3,
            font_size=27,
            color=GREEN_A,
        )
        variance_number.add_updater(
            lambda mob: mob.set_value(
                2.0 * tracker.get_value()
            )
        )
        variance_row = VGroup(
            variance_label,
            variance_number,
        ).arrange(RIGHT, buff=0.10)

        mass_formula = MathTex(
            r"\int_{\mathbb R}\Phi(x,t)\,dx=1",
            font_size=27,
            color=TEAL_A,
        )

        information = VGroup(
            t_row,
            peak_row,
            variance_row,
            mass_formula,
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT)

        information.move_to(
            panel.get_center() + DOWN * 0.25
        )

        initial_note = Text(
            "Perfil inicial",
            font_size=27,
            color=YELLOW,
        )
        initial_note.next_to(axes, DOWN, buff=0.12)

        # ------------------------------------------------------------
        # Animación
        # ------------------------------------------------------------
        self.play(
            FadeIn(title),
            Write(formula),
            run_time=1.8,
        )

        self.play(
            Create(axes),
            Write(axis_labels),
            FadeIn(panel),
            FadeIn(panel_title),
            FadeIn(information),
            run_time=2.0,
        )

        self.play(
            FadeIn(area),
            Create(curve),
            FadeIn(maximum_point),
            FadeIn(initial_note),
            run_time=2.0,
        )

        # Se conserva el dato inicial el tiempo suficiente para observarlo.
        self.wait(3.0)

        evolution_note = Text(
            "Difusión: el perfil se ensancha y su máximo disminuye",
            font_size=25,
            color=BLUE_A,
        )
        evolution_note.next_to(axes, DOWN, buff=0.12)

        self.play(
            ReplacementTransform(initial_note, evolution_note),
            tracker.animate.set_value(t_final),
            run_time=12.0,
            rate_func=linear,
        )

        final_statement = MathTex(
            r"\Phi(\cdot,t)\longrightarrow 0"
            r"\quad\text{puntualmente cuando }t\to\infty,"
            r"\qquad"
            r"\int_{\mathbb R}\Phi(x,t)\,dx=1",
            font_size=27,
        )
        final_statement.set_color_by_tex(
            r"\int_{\mathbb R}\Phi(x,t)\,dx=1",
            TEAL_A,
        )
        final_statement.next_to(axes, DOWN, buff=0.10)

        self.play(
            ReplacementTransform(
                evolution_note,
                final_statement,
            ),
            run_time=1.5,
        )

        self.wait(3.0)
