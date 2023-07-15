from MyExceptions import TimeTypeError, TimeValueError


class Time:
    def __init__(self, h, m, s):
        try:
            if type(h) != int:
                raise TimeTypeError("hour", h)
            elif type(m) != int:
                raise TimeTypeError("minute", m)
            elif type(s) != int:
                raise TimeTypeError("second", s)

            if h < 0 or h > 23:
                raise TimeValueError("hour", h)
            elif m < 0 or m > 59:
                raise TimeValueError("minute", m)
            elif s < 0 or s > 59:
                raise TimeValueError("second", s)

        except (TimeValueError, TimeTypeError) as err:
            print(err)
        else:
            self.hour = h
            self.minute = m
            self.second = s

    def __repr__(self):
        try:
            return "{}:{}:{}".format(self.hour, self.minute, self.second)
        except AttributeError:
            return "Object is empty."

    def add_hour(self, n=1):
        try:
            if type(n) != int:
                raise TimeTypeError(" param n", n)

            if n < 0:
                raise TimeValueError(" param n", n)
            self.hour = (self.hour + n) % 24
        except (TimeValueError, TimeTypeError) as err:
            print(err)
        except AttributeError:
            print("Object does not have attribute 'hour'")

    def add_minute(self, n=1):
        try:
            if type(n) != int:
                raise TimeTypeError("param n", n)

            if n < 0:
                raise TimeValueError(" param n", n)
            self.minute = (self.minute + n) % 60
            self.add_hour((self.minute + n) // 60)
        except TimeValueError as err:
            print(err)
        except TimeTypeError as err:
            print(err)
        except AttributeError:
            print("Object does not have attribute 'hour'")

    def add_second(self, n=1):
        try:
            if type(n) != int:
                raise TimeTypeError("param n", n)
            if n < 0:
                raise TimeValueError(" param n", n)
        except (TimeValueError, TimeTypeError) as err:
            print(err)
        except AttributeError:
            print("Object does not have attribute 'hour'")
        else:
            self.second = (self.second + n) % 60
            self.add_minute((self.second + n) // 60)


# t = Time('5', 10, 36)
# print(t)
# t.add_hour(6)
# t.add_hour(-2)

# t2 = Time(5, 10, 36)
# print(t2)
# t2.add_hour('6')
# t2.add_hour(-2)
