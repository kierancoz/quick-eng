from eng_core import Vector


class Force(Vector):
    def __init__(self, vector, coords = None, amount = None):
        super().__init__(list(vector))
        self.location = coords
        self.value = amount

    def __iter__(self):
        for val in [self.Fx, self.Fy, self.Fz]:
            yield val

    def __add__(self, other):
        self_list = list(self)
        other_list = list(other)
        new_list = Vector([self_list[i] + other_list[i] for i in range(3)])
        return Force(new_list, amount = new_list.magnitude)

    def __sub__(self, other):
        self_list = list(self)
        other_list = list(other)
        new_list = Vector([self_list[i] - other_list[i] for i in range(3)])
        return Force(new_list, amount = new_list.magnitude)

    # Absolute value of Force
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    # Location
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    # Forces
    @property
    def Fx(self):
        return self.X * self.value
    
    @property
    def Fy(self):
        return self.Y * self.value

    @property
    def Fz(self):
        return self.Z * self.value