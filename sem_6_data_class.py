import dataclasses
import inspect
from pprint import pprint
from dataclasses import dataclass, asdict, astuple, field


class RegClass:

    def __init__(self, _id: int, _data: str):
        # immutable fields for hash-function
        self.__id: int = _id
        self.__data: str = _data

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}, {self.data}"

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.data) == (other.id, other.data)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.data) < (other.id, other.data)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.data) <= (other.id, other.data)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.data) > (other.id, other.data)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.data) >= (other.id, other.data)
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.__class__, self.id, self.data))


@dataclass(frozen=True, order=True)
class DataClass:
    id: int
    text: str = ""  # field(default="")
    data: list[str] = field(default_factory=list)


if __name__ == '__main__':
    pprint(inspect.getmembers(DataClass, inspect.isfunction))

    instance = DataClass(1, "Some data")
    print(instance)
    print(asdict(instance))
    print(astuple(instance))

    instance_copy = dataclasses.replace(instance, id=2)

    print(instance_copy)
    print(asdict(instance_copy))
    print(astuple(instance_copy))
