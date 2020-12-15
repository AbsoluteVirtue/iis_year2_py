import functools


def decorator(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        print('decorator functionality here')
        return func(*args, **kwargs)

    return new_func


@decorator
def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(10, 20))
