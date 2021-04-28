import traceback
from db_mock import students_mock as students


def test(collection):
    return students.database.find(collection)

# re-raise / re-throw


if __name__ == '__main__':

    res, _ = test("students")
    if res:
        print(res)

    print("exit")
