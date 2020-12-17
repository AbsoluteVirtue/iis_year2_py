import xlwt

import students


def calc(first, second, attendance, *grades):
    """
        (eval 1 * 0.15) + (eval 2 * 0.15) + (median labs * 0.15) + (practice * 0.15) = 60% of final grade
    """
    def median(*args):
        return sum(args) / len(args)

    def max_(no_of_grades_to_consider, *args):
        check = list(*args)
        res = []
        while check and len(res) != no_of_grades_to_consider:
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
        'recalc_second': second,
        'final': total * 0.6,
    }

    return result


def print_out(student_list, with_projection=True):
    for _name, _group, _first, _second, _attendance, *_grades in student_list:

        _res = calc(_first, _second, _attendance, *_grades)

        print(f'{_name} ({_group})')
        print((f'\tlab: {_res["hard"]["labs"]:.2f}, '
               f'att 1: {_first:.2f}, '
               f'att 2: {_second:.2f}, '
               f'sem: {_attendance:.2f} = '
               f'{_res["hard"]["total"]:.2f}'))
        if with_projection:
            print((f'\tlab: {_res["soft"]["labs"]:.2f}, '
                   f'att 1: {_first:.2f}, '
                   f'att 2: {_res["soft"]["recalc_second"]:.2f}, '
                   f'sem: {_attendance:.2f} = '
                   f'{_res["soft"]["total"]:.2f} ({_res["hard"]["final"]:.2f}|{_res["hard"]["final"] + 40:.2f})'))


def file_out(student_list):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Grades')

    ws.write(0, 0, u"no.")
    ws.write(0, 1, u"student")
    ws.write(0, 2, u"group")
    ws.write(0, 3, u"att. 1")
    ws.write(0, 4, u"att. 2")
    ws.write(0, 5, u"lab.")
    ws.write(0, 6, u"sem.")
    ws.write(0, 7, u"truncated")
    ws.write(0, 8, u"projected")

    row = 1
    i = 0
    for __name, __group, __first, __second, __attendance, *__grades in student_list:
        __res = calc(__first, __second, __attendance, *__grades)

        ws.write(row, 0, i + 1)
        ws.write(row, 1, __name.strip(), xlwt.Style.easyxf("font: bold on"))
        ws.write(row, 2, __group.strip())
        ws.write(row, 3, f'{__first:.2f}')
        ws.write(row, 4, f'{__second:.2f}')
        ws.write(row, 5, f'{__res["hard"]["labs"]:.2f}')
        ws.write(row, 6, f'{__attendance:.2f}')
        ws.write(row, 7, f'{__res["hard"]["total"]:.2f}')
        ws.write(row, 8, f'{__res["hard"]["final"] + 40:.2f}')

        row += 1
        i += 1

    wb.save("grades.xlsx")


if __name__ == '__main__':
    # file_out()
    print_out(students.YEAR_ONE_F, False)
