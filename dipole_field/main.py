from manim import *
from manim_physics import *

from dipole_field.dipole import Dipole


def multi_line_text(text, separator=r"\n", **kwargs):
    lines = text.split(separator)
    return VGroup(*[Text(line) for line in lines]).arrange(DOWN)


def multi_line_tex(texs: list[Tex]):
    return VGroup(*texs).arrange(DOWN)


def vector_from_start_and_end(start, end, **kwargs):
    return Vector(direction=end - start, **kwargs).shift(start)


def generate_dipole(scene, dipole_size=1, play_animation=True, position=ORIGIN, direction=LEFT, generate_field=False):
    charge1 = Charge(1, direction / 2).shift(position)
    charge2 = Charge(-1, -direction / 2).shift(position)
    charge1.move_to(dipole_size * direction / 2)
    charge2.move_to(dipole_size * direction / -2)
    if play_animation:
        scene.add(charge1, charge2)
    dipole_connector = Vector(direction=dipole_size * direction, color=WHITE).shift(dipole_size * RIGHT / 2)
    dipole_connector_text = Tex("d", color=WHITE).next_to(dipole_connector, UP)
    if play_animation:
        scene.play(Create(dipole_connector), Write(dipole_connector_text))
    dipole = VGroup(charge2, charge1, dipole_connector, dipole_connector_text)
    field = ElectricField(charge1, charge2)
    if generate_field:
        scene.play(Create(field))
    return dipole, field


DIPOLE_INFO_TEXT = r"Dipole is a pair of charges with opposite signs \n separated by a small distance d"
DIPOLE_FIELD_TEXT = r"And how to find its electric field?"
DIPOLE_SOL_TEXT1 = r"Finding a field on its axis is simple. \n We should to calculate the attraction to one of the charges \n and the repulsion from the other. They are very close to each other"
PERENDICULAR_DIPOLE_INFO_TEXT = r"Similar calculation can be done if the charge \n is on a line perpendicular to the dipole "
DIPOLE_FINAL_INFO = r"Now we can calculate the field of a dipole \n in any point"


class Scene(Scene):
    def construct(self):
        dipole, field = generate_dipole(self, dipole_size=5)

        text = multi_line_text(DIPOLE_INFO_TEXT, stroke_width=0).shift(DOWN * 2).scale(0.5)
        self.play(Write(text))
        self.wait(3)
        self.remove(text)
        text = multi_line_text(DIPOLE_FIELD_TEXT, stroke_width=0).shift(DOWN * 2).scale(0.5)
        self.play(Write(text), Create(field))
        self.wait(3)
        small_dipole, _ = generate_dipole(self, dipole_size=1, play_animation=False)
        self.remove(field)
        self.play(Transform(dipole, small_dipole))
        xaxis = NumberLine(x_range=[-5, 5, 1], color=WHITE, include_numbers=True)
        point = Dot(color=WHITE).move_to(LEFT * 3)
        self.play(Create(xaxis), Create(point))

        self.remove(text)
        text = multi_line_text(DIPOLE_SOL_TEXT1, stroke_width=0).shift(DOWN * 2).scale(0.5)
        charge_field_formula = Tex(r"Single charge field: $E_{1}(x) = \frac{k q}{x^2} $", color=WHITE).shift(
            UP * 3).shift(RIGHT * 2)
        dipole_field_formula = MathTex(
            r"E_{dipole}(x) = E_{1}(x + d) - E_1(x) = \frac{\partial E_1}{\partial x} d = \frac{2kq \vec{d}}{x^2}",
            color=WHITE).shift(UP * 1.5).shift(LEFT * 0.5)
        self.play(Write(text))
        self.play(Write(charge_field_formula), Write(dipole_field_formula))

        self.wait(5)
        self.remove(text)
        text = multi_line_text(PERENDICULAR_DIPOLE_INFO_TEXT, stroke_width=0).shift(DOWN * 3).scale(0.5)
        self.play(Write(text), FadeOut(charge_field_formula), FadeOut(dipole_field_formula), FadeOut(point),
                  FadeOut(xaxis), FadeOut(small_dipole), FadeOut(dipole), FadeOut(dipole))
        self.wait(0.2)

        dipole = Dipole(1, 1, UP).shift(LEFT * 4)
        self.play(Create(dipole))
        # yaxis = NumberLine(x_range=[0, 5, 1], color=WHITE, include_numbers=True)
        # self.add(yaxis)
        point = Dot(color=YELLOW).move_to(RIGHT * 1)
        center_line = Line(dipole.get_center(), point.get_center(), color=WHITE)

        line_to_positive_charge = DashedLine(point.get_center(), dipole.positive_charge.get_center(), color=WHITE)
        line_to_negative_charge = DashedLine(point.get_center(), dipole.negative_charge.get_center(), color=WHITE)

        angle = Angle(center_line, line_to_positive_charge, radius=2, color=WHITE, quadrant=(2, 2))
        angle_text = Tex(r"$\theta$", color=WHITE).next_to(angle, UP)
        self.play(Create(point))
        self.play(Create(center_line), Create(line_to_positive_charge), Create(line_to_negative_charge), Create(angle),
                  Write(angle_text))

        perpendicular_formula = MathTex(r"E_{dipole}(x) = 2 E_1(x) sin \theta", color=WHITE).shift(UP * 3).shift(
            RIGHT * 2)
        theta_text = MathTex(r"\theta = \frac{d}{2x}", color=WHITE).next_to(perpendicular_formula, DOWN)
        perp_final = MathTex(r"E_{dipole}(x) = \frac{kq \vec{d}}{r^3}", color=WHITE).next_to(theta_text,
                                                                                             DOWN)
        self.play(Write(perpendicular_formula), Write(theta_text), Write(perp_final))
        self.wait(3)

        self.remove(text)
        text = multi_line_text(DIPOLE_FINAL_INFO, stroke_width=0).shift(DOWN * 3).scale(0.5)
        point = Dot(color=YELLOW).move_to(RIGHT * 2 + UP * 1)

        self.play(Write(text), FadeOut(perpendicular_formula), FadeOut(theta_text), FadeOut(perp_final), FadeOut(point), FadeOut(center_line), FadeOut(line_to_positive_charge), FadeOut(line_to_negative_charge), FadeOut(angle), FadeOut(angle_text))
        self.wait(0.2)
        self.wait(10)
