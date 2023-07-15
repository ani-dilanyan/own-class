from MyExceptions import RationalValueError, RationalTypeError

class Rational:
    def __init__(self, n, d):
        try:
            if type(n) != int:
                raise RationalTypeError("numerator", n)
            elif type(d) != int:
                raise RationalTypeError("denominator", d)
            if d <= 0:
                raise RationalValueError("Wrong value for denominator: 0")

        except (RationalTypeError, RationalValueError) as error:
            print(error)
        else:
            x = Rational.gcd(n, d)
            self.numerator = n // x
            self.denominator = d // x

    def __repr__(self):
        try:
            return "{}/{}".format(self.numerator, self.denominator)
        except AttributeError:
            return "Object is empty because of wrong initialisation"

    def __eq__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        try:
            if type(other) != Rational:
                raise RationalTypeError("second number", other)
            return self.numerator == other.numerator and other.denominator == self.denominator
        except RationalTypeError as error:
            return error
        except AttributeError:
            return "Object does not have required attributes"

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        try:
            if type(other) != Rational:
                raise RationalTypeError("second number", other)
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        except RationalTypeError as error:
            return error
        except AttributeError:
            return "Object does not have required attributes"

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        try:
            if type(other) != Rational:
                raise RationalTypeError("second number", other)
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        except RationalTypeError as error:
            return error
        except AttributeError:
            return "Object does not have required attributes"

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        try:
            if type(other) != Rational:
                raise RationalTypeError("second number", other)
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        except RationalTypeError as error:
            return error
        except AttributeError:
            return "Object does not have required attributes"

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        try:
            if type(other) != Rational:
                raise RationalTypeError("second number", other)
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Rational(numerator, denominator)
        except RationalTypeError as error:
            return error
        except AttributeError:
            return "Object does not have required attributes"

    def __lt__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        try:
            if type(other) != Rational:
                raise RationalTypeError("second number", other)
            num1 = self.numerator * other.denominator
            num2 = other.numerator * self.denominator
            return num1 < num2
        except RationalTypeError as error:
            return error
        except AttributeError:
            return "Object does not have required attributes"

    @staticmethod
    def gcd(x, y):
        from math import gcd
        return gcd(x, y)


# # Example usage:
# r1 = Rational(1, 2)
# r2 = Rational(3, 4)
# r3 = 2
# r4 = 'a'
# r5 = Rational(4, 2)
#
# print(r1 + r2)  # 5/4
# print(r1 - r2)  # -1/4
# print(r1 * r2)  # 3/8
# print(r1 / r2)  # 2/3
# print(r1 < r2)  # True
# print(r1 == r2)  # False
# print(r5 == r3)  # True
# print(r2 == r4)  # Unsupported type for second number <class 'str'>
# r6 = Rational('a', 7)  # Unsupported type for numerator <class 'str'>
# print(r6)  # Object is empty because of wrong initialisation
# print(r6 == r2)  # Object does not have required attributes
#
# print(Rational(-1, -2))  # 1/2
# print(Rational(-1, 0))  # Wrong value for denominator: 0
# # Object is empty because of wrong initialization
