import datetime


class TestException(Exception):

    def __init__(self, code=0, msg=""):
        self._code = code
        self._msg = msg
        self._date = datetime.datetime.now()

    def __str__(self):

        return "[{date}] {code}: {msg}".format(
            date=self._date, code=self._code, msg=self._msg)


def throw_ex():
    raise TestException(-1, "something has gone wrong")


if __name__ == '__main__':

    try:
        d = dict(x=0, y=0)

        print(d)

        throw_ex()
    except TestException as ex:
        print(ex)

    print("Through exception here")
