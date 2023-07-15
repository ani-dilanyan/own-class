from Money import Money
from datetime import datetime
from MyExceptions import TransactionTypeError, TransactionValueError


class Transaction:
    def __init__(self, money: Money, description):
        try:
            if type(description) != str:
                raise TransactionTypeError("description", description)
            elif type(money) != Money:
                raise TransactionTypeError("money", money)
        except TransactionTypeError as err:
            print(err)
        else:
            self.datetime = str(datetime.now().hour) + ":" + str(datetime.now().minute) + " " + str(
                datetime.now().date())
            self.description = description
            self.money = money
            self.status = "Pending"

    def change_status(self, new_status):
        try:
            if type(new_status) != str:
                raise TransactionTypeError("status change", new_status)
            if new_status not in ("Pending", "Approved", "Denied"):
                raise TransactionValueError("status change", new_status)
        except (TransactionTypeError, TransactionValueError) as error:
            print(error)
        else:
            self.status = new_status
