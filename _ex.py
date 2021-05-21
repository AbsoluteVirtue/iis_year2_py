import traceback
from db_mock import students_mock as students


def test(collection, t):
    # return students.database.find(collection)

    return collection / t

# re-raise / re-throw


if __name__ == '__main__':

    try:
        res = test(10, 0)
    except ZeroDivisionError as zde:
        print(zde)
    except Exception as ex:
        traceback.print_exc()
    else:
        print(res)

    print("exit")
