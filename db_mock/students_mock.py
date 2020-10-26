
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


class Db:

    _collections = {
        'students': Students(),
    }

    @property
    def students(self):
        return self._collections['students']

    def find(self, collection):
        if not self._collections.get(collection):
            raise Exception('collection does not exist')
        return self._collections.get(collection)


database = Db()
