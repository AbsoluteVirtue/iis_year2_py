import students


NUMBER_OF_GRADES_TO_CONSIDER = 4


def calc(first, second, attendance, *grades):
    """
        (eval 1 * 0.15) + (eval 2 * 0.15) + (median labs * 0.15) + (practice * 0.15) = 60% of final grade
    """
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

    second = median(*max_(NUMBER_OF_GRADES_TO_CONSIDER, grades))
    total = median(first, second, attendance, labs)

    result['soft'] = {
        'labs': labs,
        'total': total,
        'recalc_second': second,
        'final': total * 0.6,
    }

    return result


if __name__ == '__main__':
    for _name, _group, _first, _second, _attendance, *_grades in students.YEAR_ONE_EASY:
        # first, second, attendance, *grades
        _res = calc(_first, _second, _attendance, *_grades)
        print(f'{_name} ({_group})')
        print((f'\tlab: {_res["hard"]["labs"]:.2f}, '
               f'att 1: {_first:.2f}, '
               f'att 2: {_second:.2f}, '
               f'sem: {_attendance:.2f} = '
               f'{_res["hard"]["total"]:.2f} ({_res["hard"]["final"]:.2f}|{_res["hard"]["final"] + 40:.2f})'))
        print((f'\tlab: {_res["soft"]["labs"]:.2f}, '
               f'att 1: {_first:.2f}, '
               f'att 2: {_res["soft"]["recalc_second"]:.2f}, '
               f'sem: {_attendance:.2f} = '
               f'{_res["soft"]["total"]:.2f} ({_res["soft"]["final"]:.2f}|{_res["soft"]["final"] + 40:.2f})'))
