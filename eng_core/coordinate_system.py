from eng_core import Vector


class CoordinateSystem(Vector):
    def __init__(self, components):
        super().__init__(components)

    def convert_location(self, vector):
        return Vector([vector.X - self.X, vector.Y - self.Y, vector.Z - self.Z])