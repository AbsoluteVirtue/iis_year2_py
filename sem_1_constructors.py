
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

    c1 = Coordinates()
    c1.x = 1
    c1.y = 2
    c1.desc = "hello"

    c2 = Coordinates(10, 20, "world")

    print(c1)
    print(c1.__dict__)
    print(c2.__dict__)
    print(c1.print())
    print(Coordinates.print(c1))

    c2 = c1
    print(c2)

    print(Coordinates.num_of_coord)
    Coordinates.reset_num_of_coord()
    print(Coordinates.num_of_coord)

    c3 = Coordinates.from_string("Test,100,200")
    print(c3)
