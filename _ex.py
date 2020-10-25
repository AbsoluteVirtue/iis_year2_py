import datetime


class MyException(BaseException):

    def __init__(self, msg="error", code=0):
        self.msg = msg
        self.code = code
        self.t = datetime.datetime.now()

    def __str__(self):
        return "%s, %s: %s" % (self.t, self.code, self.msg)


def test_f():
    print("test")
    raise MyException("exception in test")


if __name__ == '__main__':

    try:
        test_f()
    except Exception as ex:
        print(ex)
    except MyException as ex:
        print(ex)

    print("safe return")
