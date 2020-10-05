
class Coordinates:

    num_of_coord = 0

    def __init__(self, desc="Coordinates"):
        self.desc = desc
        Coordinates.incr_num_of_coord()

    @classmethod
    def incr_num_of_coord(cls):
        cls.num_of_coord += 1

    @classmethod
    def decr_num_of_coord(cls):
        cls.num_of_coord = (cls.num_of_coord - 1 if cls.num_of_coord > 0 else 0)


class Coordinates2D(Coordinates):

    def __init__(self, x=0, y=0, desc="2D-coordinates"):
        super().__init__(desc=desc)
        self.x = x
        self.y = y

    def __len__(self):
        return self.x + self.y

    def __repr__(self):
        return 'Coordinates2D({}, {}, "{}")'.format(self.x, self.y, self.desc)

    def __str__(self):
        return "{}: {}, {}".format(self.desc, self.x, self.y)

    @classmethod
    def from_string(cls, string):
        _desc, _x, _y = string.split(',')
        return cls(x=_x, y=_y, desc=_desc)


class Coordinates3D(Coordinates):

    num_of_coord = 0

    def __init__(self, x=0, y=0, z=0, desc="3D-coordinates"):
        super().__init__(desc=desc)

        self.x = x
        self.y = y
        self.z = z


class Point2D:

    def __init__(self, coord=None):
        if coord and not coord.__dict__.get('z'):
            self.coord = coord
        else:
            self.coord = Coordinates2D()

    @property
    def desc(self):
        return self.coord.desc

    @desc.setter
    def desc(self, desc):
        self.coord.desc = desc

    @property
    def coordinates(self):
        return self.coord.x, self.coord.y

    @coordinates.setter
    def coordinates(self, coord):
        self.coord = coord

    @classmethod
    def from_tuple(cls, tup):
        return cls(Coordinates2D(x=tup[0], y=tup[1]))

    def __add__(self, other):
        return Point2D(
            Coordinates2D(
                self.coord.x + other.coord.x,
                self.coord.y + other.coord.y))

    def __repr__(self):
        return 'Point2D({})'.format(self.coord.__repr__())

    def __str__(self):
        return "{}, {}".format(self.coord.x, self.coord.y)
