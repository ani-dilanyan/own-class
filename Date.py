from MyExceptions import DateTypeError, DateValueError


class Date:
    is_valid = True
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = ['', "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    def __init__(self, day, month, year):
        try:
            if type(year) != int:
                raise DateTypeError("year", year)
            elif type(month) != int:
                raise DateTypeError("month", month)
            elif type(day) != int:
                raise DateTypeError("day", day)

            if year < 0:
                raise DateValueError("year", year)
            elif month < 0 or month > 12:
                raise DateValueError("month", month)

            if month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    self.month_days[2] = 29
            if day < 0 or day > self.month_days[month]:
                raise DateValueError("day", day)

        except (DateTypeError, DateValueError) as error:
            self.is_valid = False
            print(error)
        else:
            self.year = year
            self.month = month
            self.day = day

    def __repr__(self):
        try:
            return "{} {} {}".format(self.day, self.month_names[self.month], self.year)
        except AttributeError:
            return "Object is empty because of wrong initialisation"

    def add_year(self, n=1):
        try:
            if type(n) != int:
                raise DateTypeError("number of years to add", n)

            if n < 0:
                raise DateValueError("number of years to add", n)

            self.year += n

        except (DateValueError, DateTypeError) as error:
            print(error)
        except AttributeError:
            print("Object does not have attribute 'year'")

    def add_month(self, n=1):
        try:
            if type(n) != int:
                raise DateTypeError("number of month to add", n)

            if n < 0:
                raise DateValueError("number of month to add", n)

            self.add_year((self.month + n - 1) // 12)
            self.month = (self.month + n - 1) % 12 + 1

        except (DateTypeError, DateValueError) as error:
            print(error)
        except AttributeError:
            print("Object does not have attribute 'month'")

    def add_days(self, num_days=1):
        try:
            if type(num_days) != int:
                raise DateTypeError("number of days to add", num_days)

            if num_days < 0:
                raise DateValueError("number of days to add", num_days)

            total_days = self.day + num_days
            days_in_month = self.month_days[self.month]

            if self.month == 2:
                if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
                    days_in_month = 29

            while total_days > days_in_month:
                total_days -= days_in_month
                self.add_month(1)
                days_in_month = self.month_days[self.month]

            self.day = total_days

        except (DateTypeError, DateValueError) as error:
            print(error)
        except AttributeError:
            print("Object does not have attribute 'day'")


# my_date = Date(25, 6, 2023)
# print(my_date)  # 25 Jun 2023
#
# my_date.add_days(10)
# print(my_date)  # 5 Jul 2023
#
# my_date.add_year(3)
# my_date.add_month(8)
# print(my_date)  # 5 Mar 2027
#
# my_date.add_days(365)
# print(my_date)  # 5 Mar 2026

# my_date2 = Date(35, 6, 2023)  # Wrong value for day: 35
# print(my_date2)  # Object is empty because of wrong initialisation

# my_date3 = Date(25, 26, 2023)  # Wrong value for month: 26
# print(my_date3)  # Object is empty because of wrong initialisation

# my_date4 = Date(25, 6, -2023)  # Wrong value for year: -2023
# print(my_date4)  # Object is empty because of wrong initialisation

# my_date5 = Date('35', 6, 2023)  # Unsupported type for day: <class 'str'>
# my_date6 = Date(25, (6, 25), 2023)  # Unsupported type for month: <class 'tuple'>
# my_date7 = Date(25, 6, [2023])  # Unsupported type for month: <class 'list'>

# my_date.add_days(-10) # Wrong value for number of days to add: -10
# my_date.add_month(-10) # Wrong value for number of month to add: -10
# my_date.add_year(-10) # Wrong value for number of years to add: -10
