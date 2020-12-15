import students


def calc(name, first, second, attendance, *grades):
    """
        (eval 1 * 0.15) + (eval 2 * 0.15) + (median labs * 0.15) + (practice * 0.15) = 60% of final grade
    """
    print(f'{name}')

    def median(*args):
        return sum(args) / len(args)

    def max_(no, *args):
        check = list(*args)
        res = []
        while check and len(res) != no:
            m = max(*check)
            res.append(m)
            check.remove(m)

        return tuple(res)

    labs = median(*grades)
    total = median(first, second, attendance, labs)

    result = {
        'hard': {
            'labs': labs,
            'total': total,
            'final': total * 0.6,
        },
    }

    second = median(*max_(3, grades))
    total = median(first, second, attendance, labs)

    result['soft'] = {
        'labs': labs,
        'total': total,
        'final': total * 0.6,
    }

    return result


if __name__ == '__main__':
    calc("bogaciov", 80, 87.5, 100, *(100, 85, 80, 90))
    print(f'lab: {labs:.2f}, att 1: {first:.2f}, att 2: {second:.2f}, sem: {attendance:.2f} = {total:.2f} ({final:.2f}|{final + 40:.2f})')
    print(f'lab: {labs:.2f}, att 1: {first:.2f}, att 2: {second:.2f}, sem: {attendance:.2f} = {total:.2f} ({final:.2f}|{final + 40:.2f})')
