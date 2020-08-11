

class Vector(object):
    def __init__(self, components):
        self.__components = components

    def __iter__(self):
        for comp in self.__components:
            yield comp

    @property
    def X(self):
        return self.__components[0]

    @property
    def Y(self):
        return self.__components[1]

    @property
    def Z(self):
        return self.__components[2]

    @property
    def magnitude(self):
        return (self.Y**2 + self.X**2 + self.Z**2)**(1/2)

    @property
    def unit_vector(self):
        distance = self.magnitude
        return Vector([self.X/distance, self.Y/distance, self.Z/distance])
