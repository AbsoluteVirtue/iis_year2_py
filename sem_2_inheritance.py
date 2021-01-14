import collections
import logging


class LoggingDict(dict):

    def __setitem__(self, key, value):
        logging.info('Set %s to %s' % (key, value))
        super().__setitem__(key, value)


class LoggingOrderedDict(LoggingDict, collections.OrderedDict):
    # resolution order: LoggingDict, OrderedDict, dict, object
    pass


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
        return cls(x, y, desc)


class Coordinates3D(Coordinates):

    num_of_coord = 0

    def __init__(self, x=0, y=0, z=0, desc=""):
        super().__init__(x, y, desc)
        Coordinates.decr_num_of_coord()

        self.z = z
        Coordinates3D.incr_num_of_coord()


if __name__ == '__main__':

    s = Coordinates3D(1.1, 2.2, 3.3, "hello 3D")
    print(s)
    print(help(Coordinates3D))

    print(LoggingOrderedDict.__mro__)
