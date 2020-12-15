
def calc(name, attendance, first, second, *args):
    """
        (eval 1 * 0.15) + (eval 2 * 0.15) + (median labs * 0.15) + (practice * 0.15) = 60% of final grade
    """
    def median(*arguments):
        return sum(*arguments) / len(arguments)

    total = (first + second + attendance + median(args)) * 0.6
    print(f'{name} {total/4}')
    print(f'----->{median(attendance * 0.15, first * 0.15, second * 0.15, median(args) * 0.15)}')


if __name__ == '__main__':
    calc("bogaciov", 100, 80, 87.5, *(100, 85, 80, 90))
