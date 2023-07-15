from MyExceptions import MoneyTypeError, MoneyValueError


# Create class 'Money'
class Money:
    # define supported currencies and their exchange rates as a dictionary
    EXCHANGE_RATE = {"AMD": 1, "RUB": 4, "USD": 400, "EUR": 420}

    # Initialize data members if types and values given as arguments are valid,
    # otherwise raise corresponding errors
    def __init__(self, currency, amount):
        try:
            # check if types of currency and amount are valid
            if type(currency) != str:
                raise MoneyTypeError("currency", currency)
            elif type(amount) != int and type(amount) != float:
                raise MoneyTypeError("amount", amount)

            # check if values of currency and amount are valid
            if currency not in self.EXCHANGE_RATE:
                raise MoneyValueError("currency", currency)
            elif amount < 0:
                raise MoneyValueError("amount", amount)
        except (MoneyValueError, MoneyTypeError) as error:
            print(error)
        else:
            # if values and their types are valid initialise them to corresponding attributes
            self.currency = currency
            self.amount = amount

    # Overwrite repr to return 'amount' and 'currency' attributes
    def __repr__(self):
        try:
            return "{:.2f} {}".format(self.amount, self.currency)
        except AttributeError:
            return "Object is empty"

    # Create a method to exchange money, which searches for a currency to exchange
    # in the EXCHANGE_RATE dictionary and returns a new Money object
    def exchange(self, currency):
        try:
            if type(currency) != str:
                raise MoneyTypeError("currency", currency)

            if currency not in self.EXCHANGE_RATE:
                raise MoneyValueError("currency", currency)

        except (MoneyValueError, MoneyTypeError) as error:
            print(error)
            return "Exchange failed"
        except AttributeError:
            print("Object does not have attribute 'amount'")
            return "Exchange failed"
        else:
            rate = Money.EXCHANGE_RATE[self.currency] / Money.EXCHANGE_RATE[currency]
            return Money(currency, rate * self.amount)

    def __add__(self, other):
        try:
            if type(other) != Money:
                raise MoneyTypeError("money to add", other)
        except MoneyTypeError as err:
            print(err)
            return "Addition failed"
        except AttributeError:
            print("Object does not have essential attributes")
            return "Addition failed"
        else:
            if self.currency != other.currency:
                other = other.exchange(self.currency)
            return Money(self.currency, self.amount + other.amount)

    def __sub__(self, other):
        try:
            if type(other) != Money:
                raise MoneyTypeError("money to subtract", other)
            if self.amount - other.exchange(self.currency).amount < 0:
                raise MoneyValueError("money to subtract " + other.currency, other.amount)
        except (MoneyTypeError, MoneyValueError) as err:
            print(err)
            return "Subtraction failed"
        except AttributeError:
            print("Object does not have essential attributes")
            return "Subtraction failed"
        else:
            other = other.exchange(self.currency)
            return Money(self.currency, self.amount - other.amount)

    # def deposit(self, p, n):
    #     try:
    #         if type(p) != int:
    #             raise MoneyTypeError("percentage", p)
    #         elif type(n) != int:
    #             raise MoneyTypeError("years", n)
    #
    #         if p < 0:
    #             raise MoneyValueError("percentage", p)
    #         elif n < 0:
    #             raise MoneyValueError("years", n)
    #     except (MoneyValueError, MoneyTypeError) as error:
    #         print(error)
    #         return "Deposit is not possible"
    #     except AttributeError:
    #         print("Object does not have essential attributes")
    #         return "Deposit is not possible"
    #     else:
    #         return Money(self.currency, self.amount * ((1 + p / 100) ** n))

    def __mul__(self, n):
        try:
            if type(n) != int:
                raise MoneyTypeError("multiplier", n)
            elif n < 0:
                raise MoneyValueError("multiplier", n)
        except (MoneyTypeError, MoneyValueError) as err:
            print(err)
            return "Multiplication failed"
        except AttributeError:
            print("Object does not have essential attributes")
            return "Multiplication failed"
        else:
            return Money(self.currency, self.amount * n)

    def __lt__(self, other):
        try:
            if type(other) != Money:
                raise MoneyTypeError("other", other)
        except MoneyTypeError as err:
            return err
        except AttributeError:
            return "Object does not have essential attributes"
        else:
            if self.currency != other.currency:
                other = other.exchange(self.currency)
            return self.amount < other.amount

    def __eq__(self, other):
        try:
            if type(other) != Money:
                raise MoneyTypeError("other", other)
        except MoneyTypeError as err:
            return err
        except AttributeError:
            return "Object does not have essential attributes"
        else:
            if self.currency != other.currency:
                other = other.exchange(self.currency)
            return self.amount == other.amount

# init tests
# m = Money('RUB', 100)
# m = Money('rub', 200)
# m = Money(['rub'], 200)
# m = Money("USD", -300)
# m = Money("USD", 'a')
# print(m)

# exchange tests
# m = Money('RUB', 100)
# print(m.exchange("USD"))
# print(m.exchange('usd'))
# print(m.exchange(6))


# add tests
# m1 = Money('RUB', 100)
# m2 = Money('RUB', 200)
# print(m2 + m1)

# m2 = Money('USD', 200)
# print(m2 + m1)

# m2 = 25
# print(m1 + m2)

# m2 = "a"
# print(m1 + m2)


# subtraction tests
# m1 = Money('RUB', 100)
# m2 = Money('RUB', 200)
# print(m2 - m1)
# print(m1 - m2)

# m2 = "a"
# print(m1 - m2)

# m2 = Money('USD', 200)
# print(m2 - m1)
# print(m1 - m2)

# m2 = 25
# print(m1 - m2)

# deposit tests
# m = Money('RUB', 100)
# print(m.deposit(10, 2))
# print(m.deposit(-10, 2))
# print(m.deposit(10, -2))
# print(m.deposit('10', -2))
# print(m.deposit(10, [3]))

# m1 = Money('RUB', -100)
# print(m1 * 3)
# print(m1 * 3.5)
# print(m1 * (-3))
