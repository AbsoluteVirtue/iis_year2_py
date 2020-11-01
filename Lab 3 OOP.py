
class Date:
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    def __init__(self, day, month, year):

        self.day = day
        self.month = month
        self.year = year

    def __str__(self):

        return '({} . {} . {})'.format(
            self.day, self.month, self.year)

    def __add__(self, other):

        day = self.day + other.day
        month = self.month + other.month
        year = self.year + other.year

        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            self.months[2] = 29
        else:
            self.months[2] = 28

        if month > 12:
            month -= 12
            year += 1

        if day > self.months[month]:
            day -= self.months[month]
            month += 1
            if month > 12:
                month -= 12
                year += 1

        return Date(day, month, year)

    def __iadd__(self, other):

        self.day += other.day
        self.month += other.month
        self.year += other.year
        if self.year % 4 == 0 \
                and self.year % 100 != 0 \
                or self.year % 400 == 0:
            self.months[2] = 29
        else:
            self.months[2] = 28

        if self.month > 12:
            self.month -= 12
            self.year += 1

        if self.day > self.months[self.month]:
            self.day -= self.months[self.month]
            self.month += 1
            if self.month > 12:
                self.month -= 12
                self.year += 1

        return self

    def __sub__(self, other):

        day = self.day-other.day
        month = self.month-other.month
        year = self.year-other.year
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            self.months[2] = 29
        else:
            self.months[2] = 28
        if month < 0:
            month = month+12
            year -= 1
        elif month == 0:
            month = 12
            year -= 1
        if day < 0:
            day = day + self.months[month]
            month -= 1
            if month < 0:
                month = 12+month
                year -= 1
                
        return Date(day, month, year)
    
    def __isub__(self, other):
        self.day -= other.day
        self.month -= other.month
        self.year -= other.year
        if self.year % 4 == 0 \
                and self.year % 100 != 0 \
                or self.year % 400 == 0:
            self.months[2] = 29
        else:
            self.months[2] = 28

        if self.month < 0:
            self.month = self.month+12
            self.year -= 1
        elif self.month == 0:
            self.month = 12
            self.year -= 1

        if self.day < 0:
            self.day = self.day+self.months[self.month]
            self.month -= 1
            if self.month < 0:
                self.month = 12+self.month
                self.year -= 1

        return self


if __name__ == '__main__':

    x = Date(25, 11, 2019)
    print(x)
    y = Date(7, 1, 1)
    print(y)
    print(x + y)
    x += y
    print(x)
    print(x - y)
    x -= y
    print(x)
