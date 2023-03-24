import warnings
import numpy as np
from manim import VGroup, WHITE, Vector, ORIGIN
from manim import *
from manim_physics import Charge


def vector_from_start_and_end(start, end, **kwargs):
    return Vector(direction=end - start, **kwargs).shift(start)


class Dipole(VGroup):
    def __init__(self, size: float, magnitude: float, direction: np.ndarray,  **kwargs):
        self.size = size
        self.direction = direction
        self._negative_charge = Charge(-magnitude, direction / 2)
        self._positive_charge = Charge(magnitude, -direction / 2)
        self._dipole_connector = vector_from_start_and_end(self._negative_charge.get_center(),
                                                           self._positive_charge.get_center(), color=WHITE)
        if magnitude < 0:
            warnings.warn("Dipole with negative charge created.")
        super().__init__(self._negative_charge, self._positive_charge, self._dipole_connector, **kwargs)

    @property
    def positive_charge(self):
        return self.submobjects[1]

    @property
    def negative_charge(self):
        return self.submobjects[0]

    @property
    def dipole_connector(self):
        return self.submobjects[2]

    def get_center(self):
        return (self.positive_charge.get_center() + self.negative_charge.get_center()) / 2

    @property
    def charges(self):
        return self.positive_charge, self.negative_charge
