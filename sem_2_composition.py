
class Coordinates:

    num_of_coord = 0

    def __init__(self, x=0, y=0, desc=""):
        self.x = x
        self.y = y
        self.desc = desc
        Coordinates.incr_num_of_coord()

    def __str__(self):
        return self.print()

    def print(self):
        return "{}: {}, {}".format(self.desc, self.x, self.y)

    @classmethod
    def incr_num_of_coord(cls):
        cls.num_of_coord += 1

    @classmethod
    def decr_num_of_coord(cls):
        cls.num_of_coord = (cls.num_of_coord - 1 if cls.num_of_coord > 0 else 0)

    @classmethod
    def from_string(cls, string):
        desc, x, y = string.split(',')
        return cls(desc, x, y)


class Coordinates3D(Coordinates):

    num_of_coord = 0

    def __init__(self, x=0, y=0, z=0, desc=""):
        super().__init__(x, y, desc)

        self.z = z


class Point:

    def __init__(self, coord=None):
        if coord and not coord.__dict__.get('z'):
            self.coord = coord
        else:
            self.coord = Coordinates()

    def __add__(self, other):
        return Point(Coordinates(self.coord.x + other.coord.x,
                                 self.coord.y + other.coord.y))

    def __str__(self):
        return "{}, {}".format(self.coord.x, self.coord.y)


if __name__ == '__main__':

    # print(help(Coordinates3D))

    s = Coordinates3D(1.1, 2.2, 3.3, "hello 3D")
    print(s)

    p1 = Point(s)
    print(p1.coord)
