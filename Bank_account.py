import datetime
from CustomerData import CustomerData
from Money import Money
from Transaction import Transaction
from DateTime import DateTime
from Rational import Rational
from MyExceptions import MoneyTypeError, TransactionTypeError, TransactionValueError, CustomerDataValueError, \
    CustomerDataTypeError, MoneyValueError, RationalTypeError, TimeValueError, TimeTypeError
from Date import Date
from Time import Time


class BankAccount:
    def __init__(self, customer: CustomerData, date, time, currency):
        try:
            if type(customer) != CustomerData:
                raise CustomerDataTypeError("customer", customer)
            elif type(currency) != str:
                raise CustomerDataTypeError("currency", currency)
            elif type(date) != Date:
                raise CustomerDataTypeError("date", date)
            elif type(time) != Time:
                raise CustomerDataTypeError("time", time)

            if currency not in ("AMD", "RUB", "USD", "EUR"):
                raise CustomerDataValueError("currency", currency)
        except (CustomerDataTypeError, CustomerDataValueError) as error:
            print(error)
        else:
            self.__customer = customer
            self.__balance = Money(currency, 0)
            self.created_at = DateTime(date, time)

            self.locked_until = None
            self.login_attempts = 0
            self.__transactions_history = []
            self.__deposits = []
            self._limit = Money("USD", 1000)

    def __repr__(self):
        try:
            return "Client name: {} {}\nE-mail: {}\nPhone number: {}\n".format(self.__customer.firstname,
                                                                               self.__customer.lastname,
                                                                               self.__customer.email,
                                                                               self.__customer.phone_number)
        except AttributeError:
            return "Object is empty. Account setup is incomplete"

    def verification(self):
        if self.locked_until and self.locked_until > datetime.datetime.now():
            print("Account locked until {}".format(self.locked_until))
            return False

        while self.login_attempts < 3:
            input_password = input("Enter your password: ")
            if input_password == self.__customer.password:
                self.login_attempts = 0
                return True
            else:
                self.login_attempts += 1
                print("Wrong password. Please try again.")

        self.login_attempts = 0
        self.locked_until = datetime.datetime.now() + datetime.timedelta(minutes=5)
        print("Too many failed login attempts. Account locked until {}".format(self.locked_until))
        return False

    def transfer_to_another_account(self, output_account, money_to_transfer, description="EPOS TRANSACTION"):
        if not self.verification():
            return "Request failed"
        try:
            if type(output_account) != BankAccount:
                raise CustomerDataTypeError("output account", output_account)
            elif type(money_to_transfer) != Money:
                raise MoneyTypeError("money to transfer", money_to_transfer)

            if self.__balance < money_to_transfer:
                raise MoneyValueError("money to transfer. Insufficient funds", money_to_transfer)
            elif money_to_transfer > self._limit:
                raise MoneyValueError("money to transfer. Limit reached.", money_to_transfer)
        except (CustomerDataTypeError, MoneyTypeError, MoneyValueError) as err:
            return err
        else:
            self.__balance -= money_to_transfer
            output_account.__add__(money_to_transfer)
            self.__transactions_history.append(Transaction(money_to_transfer, description))
            return "Transfer completed successfully "

    def __add__(self, amount: Money):
        try:
            if type(amount) != Money:
                raise MoneyTypeError("money to add", amount)
        except MoneyTypeError as error:
            return error
        else:
            self.__balance += amount

    def __sub__(self, amount: Money):
        if not self.verification():
            return "Request failed"
        try:
            if type(amount) != Money:
                raise MoneyTypeError("money to add", amount)

            if amount.amount < 0 or amount > self.__balance:
                raise MoneyValueError("amount to withdraw", amount)

        except (MoneyTypeError, MoneyValueError) as error:
            return error
        else:
            self.__balance -= amount

    def deposit(self, money_to_deposit, p, n):
        try:
            if type(money_to_deposit) != Money:
                raise MoneyTypeError("money to deposit", money_to_deposit)
            if money_to_deposit < Money("USD", 50):
                raise MoneyValueError("money to deposit. Should be at least 50 USD", money_to_deposit)
        except (MoneyTypeError, MoneyValueError) as err:
            return err
        else:
            self.__deposits.append(money_to_deposit)
            result_after_n_years = Money(money_to_deposit.currency, money_to_deposit.amount * ((1 + p / 100) ** n))
            return "Current balance is {}\nAfter {} years it will be {}".format(
                money_to_deposit, n, result_after_n_years)

    def calculate_interest(self, interest_rate, time_period):
        try:
            if type(interest_rate) != Rational:
                raise RationalTypeError("interest rate", interest_rate)
            if type(time_period) != int:
                raise TimeTypeError("time period", time_period)

            if interest_rate < 0:
                raise TransactionValueError("interest rate", interest_rate)
            if time_period < 0:
                raise TimeValueError("time period", time_period)

            interest_amount = self.__balance * interest_rate * time_period
            return interest_amount
        except (TransactionTypeError, ValueError) as err:
            return err

    def freeze_account(self):
        if not self.verification():
            return "Request failed"
        self.locked_until = datetime.datetime.max
        return "Account frozen successfully"

    def activate_account(self):
        login_attempts = 0

        while login_attempts < 3:
            input_password = input("Enter your password: ")
            if input_password == self.__customer.password:
                self.locked_until = None
                return "Account activated successfully"
            else:
                login_attempts += 1
                print("Wrong password. Please try again.")
        if login_attempts >= 3:
            return "Too many failed login attempts. Account locked until {}".format(self.locked_until)

    def get_balance(self):
        if self.verification():
            return self.__balance
        else:
            return "Request failed"

    def get_transactions_history(self):
        try:
            if self.__transactions_history:
                transactions_str = ""
                for transaction in self.__transactions_history:
                    transactions_str += "{} {} {} {}".format(
                        transaction.money, transaction.description,
                        transaction.status, transaction.datetime) + "\n"
            else:
                transactions_str = "No transactions to show"
        except AttributeError:
            return "Account setup is incomplete"
        else:
            return "Transactions:\n" + transactions_str

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit_money):
        try:
            if type(limit_money) != Money:
                raise MoneyTypeError("money limit", limit_money)
        except MoneyTypeError as error:
            print(error)
        else:
            self._limit = limit_money

    def change_password(self):
        if not self.verification():
            return "Request failed"

        new_password = input("Enter your new password: ")
        self.__customer.password = new_password
        return "Password changed successfully"


b1 = BankAccount(CustomerData("Name", "Surname", Date(10, 1, 2000), "example1@gmail.com", "password_1", "11111111",
                              "PN111111"), Date(12, 7, 2023), Time(11, 13, 0), "USD")
b2 = BankAccount(
    CustomerData("FN2", "LN2", Date(20, 2, 2000), "example2@gmail.com", "password_2", "222222222", "PN2222222"),
    Date(12, 7, 2020), Time(11, 13, 0), "AMD")

# print(b2)
# print(b1.verification())
# print(b1.get_balance())
# b1.limit = Money("USD", 700)
# print(b1.limit)
# print(b1.get_transactions_history())
# b1.change_password()
# b1 + Money("USD", 50)
# b1 - Money("USD", 20)
# print(b1.get_balance())
# print(b1.deposit(Money("USD", 100), 10, 2))
# print(b1.freeze_account())
# print(b1.activate_account())
