from manim import *
from manim_physics import *
from dipole import Dipole


final_shift = np.array([0, 3, 0])
class MainScene(Scene):
    def construct(self):
        d = Dipole(size=0.2, magnitude=3, direction=UP).shift(LEFT * 4)
        charged_particle = Charge(magnitude=0.2).shift(RIGHT * 3)
        field = ElectricField(*d.charges, charged_particle)
        center_line = DashedLine(d.get_center(), charged_particle.get_center(), color=GRAY_BROWN)
        trajectory = CurvedArrow(charged_particle.get_center(), d.get_center() + final_shift, color=RED, tip_length=0.2)

        self.add(d, charged_particle, field, center_line, trajectory)

        distance_end = DashedLine(d.get_center(), d.get_center() + final_shift, color=GRAY_BROWN)
        self.add(distance_end)

