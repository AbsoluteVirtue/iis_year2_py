
class Students:

    _table = [
        {
            'name': 'Ivan Petrov',
            'group': 'MI-192',
            'grade': '7.9',
            'private': False,
        },
        {
            'name': 'Petr Ivanov',
            'group': 'MI-192',
            'grade': '8.5',
            'private': True,
        }
    ]

    def find(self, **kwargs):
        if kwargs:
            return [row for row in self._table for k, v in kwargs.items()
                    if row.get(k) == v]
        else:
            return self._table

    def count(self, **kwargs):
        return len(self.find(**kwargs))


class MyException(ZeroDivisionError):

    _args = []
    msg = "division by zero, args: %s"

    def __init__(self, *args):
        self._args = args

    def __str__(self):
        return self.msg % str(self._args)


class Db:

    _collections = {
        'students': Students(),
    }

    @property
    def students(self):
        return self._collections['students']

    def find(self, collection):
        if not self._collections.get(collection):
            return None, "no such collection exists"
        return self._collections.get(collection), None


database = Db()
