import copy


class Coordinates:

    # перегрузка метода инициализации (конструктор по умолчанию)
    def __init__(self, x=0, y=0, desc=""):
        self.x = x
        self.y = y
        self.desc = desc

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
    c1 = Coordinates()

    # прямой вызов мутаторов (setter)
    c1.x = 1
    c1.y = 2
    c1.desc = "hello"

    # вывод состояния объекта через наследуемый метод
    print(c1.__dict__)

    # прямой выхов параметрического конструктора
    c2 = Coordinates(10, 20, "world")

    # вывод состояния объекта через свой метод явно
    print(Coordinates.print(c2))

    # присваивание по ссылке (shallow copy)
    c3 = c2

    # вывод состояния объекта через перегруженный метод __str__ неявно
    print(c3)

    # изменение состояния по ссылке
    c3.desc = "test mod state"

    # инициализация массива объектов
    array = [c1, c2, c3]

    # вывод элементов массива, используя интерфейс класса list
    for c in array:
        print("-->%s" % c)

    # альтернативный "конструктор" для инициализации объекта из строки
    c4 = Coordinates.from_string("Test,100,200")

    # присваивание по значению (deep copy)
    c3 = copy.deepcopy(c4)

    # изменение состояния по значению
    c3.desc = "world"

    # добавление элемента в массив
    array.append(c4)

    # вывод элементов массива, используя итератор enumerate
    for i, c in enumerate(array):
        print("%s->%s" % (i + 1, c))
