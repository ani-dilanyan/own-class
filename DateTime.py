from Date import Date
from Time import Time
from MyExceptions import DateTypeError, TimeTypeError


class DateTime:
    def __init__(self, date, time):
        try:
            if type(date) != Date:
                raise DateTypeError("date", type(date))
            elif type(time) != Time:
                raise TimeTypeError("time", time)
        except (TimeTypeError, DateTypeError) as err:
            print(err)
        else:
            self.date = date
            self.time = time

    def __repr__(self):
        try:
            return "Date {}\nTime {}".format(self.date, self.time)
        except AttributeError:
            return "Object is empty."

    def add_second(self, second=1):
        self.time.add_second(second)

    def add_minute(self, minute=1):
        self.time.add_minute(minute)

    def add_hour(self, hour=1):
        self.date.add_days((self.time.hour + hour) // 24)
        self.time.add_hour(hour)

    def add_days(self, days=1):
        self.date.add_days(days)

    def add_month(self, months=1):
        self.date.add_month(months)

    def add_year(self, years=1):
        self.date.add_year(years)


# d1 = 'Date(25, 6, 2023)'
# t1 = Time(5, 10, 26)
# dt1 = DateTime(d1, t1)  # unsupported type for date: <class 'str>
# print(dt1)  # Object is empty
#
# d2 = Date('25', 6, 2023)
# t2 = Time(5, '10', 26)
# dt2 = DateTime(d2, t2)
# print(dt2)
#
# d3 = Date(25, 6, 2023)
# t3 = Time(5, 10, 26)
# dt3 = DateTime(d3, t3)
# print(dt3)
#
# dt3.add_days(10)
# dt3.add_year(1)
# dt3.add_month(6)
# dt3.add_second(62)
# dt3.add_minute(59)
# dt3.add_hour(20)
# print(dt3)
