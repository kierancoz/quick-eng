from eng_core import Vector


class Force(Vector):
    def __init__(self, vector, magnitude = None):
        super().__init__(vector)
        self.value = magnitude

    def __iter__(self):
        super_iter = super().__iter__()
        while(True):
            try:
                yield next(super_iter) * self.value
            except StopIteration:
                break

    def __add__(self, other):
        self_list = list(self)
        other_list = list(other)
        new_list = Vector([self_list[i] + other_list[i] for i in range(3)])
        return Force(new_list, magnitude = new_list.magnitude)

    def __sub__(self, other):
        self_list = list(self)
        other_list = list(other)
        new_list = Vector([self_list[i] - other_list[i] for i in range(3)])
        return Force(new_list, magnitude = new_list.magnitude)

    # Absolute value of Force
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    # Forces
    @property
    def Fx(self):
        return list(self)[0]
    
    @property
    def Fy(self):
        return list(self)[1]

    @property
    def Fz(self):
        return list(self)[2]