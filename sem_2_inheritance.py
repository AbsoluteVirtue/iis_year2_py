
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
    def reset_num_of_coord(cls):
        cls.num_of_coord = 0

    @classmethod
    def from_string(cls, string):
        desc, x, y = string.split(',')
        return cls(desc, x, y)


if __name__ == '__main__':

    pass
