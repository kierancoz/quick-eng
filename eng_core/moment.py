import copy
import numpy
from eng_core import Force, Vector


class Moment(Force):
    def __init__(self, coords = None, vector = None, amount = None):
        super().__init__(coords, vector, amount)

    def __iter__(self):
        for val in [self.value * coeff for coeff in list(self.moment_coefficients)]:
            yield val

    @staticmethod
    def to_moment(force):
        moment = copy.deepcopy(force)
        moment.__class__ = Moment
        return moment

    @property
    def moment_coefficients(self):
        return Vector(list(numpy.cross(list(self.location), list(self.unit_vector))))