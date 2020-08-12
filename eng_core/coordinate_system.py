from eng_core import Vector


class CoordinateSystem(Vector):
    def __init__(self, components):
        super().__init__(components)
        self.__conversion_factor = 1

    def convert_units(self, new_factor):
        self.__conversion_factor = self.__conversion_factor * new_factor
        self.components = [comp * new_factor for comp in list(self)]

    def convert_location(self, vector):
        converted = Vector([comp * self.__conversion_factor for comp in list(vector)])
        return Vector([converted.X - self.X, converted.Y - self.Y, converted.Z - self.Z])