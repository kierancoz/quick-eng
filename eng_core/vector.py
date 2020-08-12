

class Vector(object):
    def __init__(self, components):
        self.components = list(components)

    def __iter__(self):
        for comp in self.__components:
            yield comp

    @property
    def components(self):
        return self.__components

    @components.setter
    def components(self, components):
        self.__components = components

    @property
    def X(self):
        return self.components[0]

    @property
    def Y(self):
        return self.components[1]

    @property
    def Z(self):
        return self.components[2]

    @property
    def magnitude(self):
        return (self.Y**2 + self.X**2 + self.Z**2)**(1/2)

    @property
    def unit_vector(self):
        distance = self.magnitude
        return Vector([self.X/distance, self.Y/distance, self.Z/distance])
