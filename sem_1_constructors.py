import copy


class Coordinates:

    # перегрузка метода инициализации (конструктор по умолчанию)
    def __init__(self, x=0, y=0, desc=""):
        self.x = x
        self.y = y
        self.desc = desc

    # перегрузка специального метода, возвращающего длину объекта
    def __len__(self):
        return self.x + self.y

    # перегрузка специального метода вывода (например, для отладки)
    def __repr__(self):
        return 'Coordinates({}, {}, "{}")'.format(self.x, self.y, self.desc)

    # перегрузка метода вывода
    def __str__(self):
        return self.print()

    # свой метод для вывода
    def print(self):
        return "{}: {}, {}".format(self.desc, self.x, self.y)

    # метод, инициализирующий объект из строки
    @classmethod
    def from_string(cls, string):
        _desc, _x, _y = string.split(',')
        return cls(x=_x, y=_y, desc=_desc)


if __name__ == '__main__':

    # прямой вызов конструктора по умолчанию
    coord1 = Coordinates()

    # прямой вызов мутаторов (setter)
    coord1.x = 1
    coord1.y = 2
    coord1.desc = "hello"

    # вывод состояния объекта через наследуемый метод
    print(coord1.__dict__)

    # прямой вызов параметрического конструктора
    coord2 = Coordinates(10, 20, "world")

    # вывод состояния объекта через свой метод явно
    print(Coordinates.print(coord2))

    # присваивание по ссылке (shallow copy)
    coord3 = coord2

    # вывод состояния объекта через перегруженный метод __str__ неявно
    print(coord3)

    # изменение состояния по ссылке
    coord3.desc = "test mod state"

    # инициализация массива объектов
    arr = [coord1, coord2, coord3]

    # вывод элементов массива, используя интерфейс класса list
    for coord in arr:
        print("-->%s" % coord)

    # альтернативный "конструктор" для инициализации объекта из строки
    coord4 = Coordinates.from_string("test,100,200")

    # присваивание по значению (deep copy)
    coord5 = copy.deepcopy(coord4)

    # изменение состояния по значению
    coord5.desc = "world"

    # добавление элемента в массив
    arr.append(coord4)
    arr.append(coord5)

    # вывод элементов массива, используя итератор enumerate
    for i, coord in enumerate(arr):
        print("%s->%s" % (i + 1, coord))
