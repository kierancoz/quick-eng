import copy
import numpy
from eng_core import Force, Vector


class Moment(Force):
    def __init__(self, coords = None, vector = None, magnitude = None):
        super().__init__(vector, magnitude)
        self.location = Vector(coords)

    def __iter__(self):
        for val in [self.value * coeff for coeff in list(self.moment_coefficients)]:
            yield val

    def __add__(self, other):
        self_list = list(self)
        other_list = list(other)
        return Vector([self_list[i] + other_list[i] for i in range(3)])

    def __sub__(self, other):
        self_list = list(self)
        other_list = list(other)
        return Vector([self_list[i] - other_list[i] for i in range(3)])

    @staticmethod
    def to_moment(force, coords = None):
        moment = copy.deepcopy(force)
        moment.__class__ = Moment
        moment.location = coords
        return moment

    @property
    def moment_coefficients(self):
        return Vector(list(numpy.cross(list(self.location), list(self.unit_vector))))

    # Location
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    # Moments
    def Mx(self):
        return list(self)[0]
    
    def My(self):
        return list(self)[1]

    def Mz(self):
        return list(self)[2]