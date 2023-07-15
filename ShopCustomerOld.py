import datetime
from Money import Money
from Person import Person
from Product import Product
from MyExceptions import CustomerDataTypeError, CustomerDataValueError
from prices import prices
from Date import Date
from Time import Time
from Purchase import Purchase
from Bank_account import BankAccount
from CustomerData import CustomerData


class CustomerAccount(Person):
    def __init__(self, firstname, lastname, birthday, email, password, phone_number):
        super().__init__(firstname, lastname, birthday)
        try:
            if type(email) != str:
                raise CustomerDataTypeError("email", email)
            elif type(password) != str:
                raise CustomerDataTypeError("password", password)
            elif type(phone_number) != str:
                raise CustomerDataTypeError("phone number", phone_number)

            if len(phone_number) < 8:
                raise CustomerDataValueError("Phone number. Must contain 8 characters after after country code",
                                             phone_number)
        except (CustomerDataValueError, CustomerDataTypeError) as err:
            print(err)
        else:
            self.email = email
            self.__password = password
            self.phone_number = phone_number
            self.created_at = datetime.datetime.now()
            self.order_history = []
            self.cart_items = []
            self.favourite_products = []
            self.purchase_history = []

    def __repr__(self):
        try:
            return "Client name: {} {}\nE-mail: {}\nPhone number: {}\n".format(self.firstname, self.lastname,
                                                                               self.email, self.phone_number)
        except AttributeError:
            return "Object is empty. Account setup is incomplete"

    def add_to_cart(self, product_title, product_quantity):
        for product in self.cart_items:
            if product_title == product["product_details"].title:
                product["quantity"] += product_quantity
                return "Product successfully added to cart"

        self.cart_items.append({"product_details": Product(product_title, prices[product_title]),
                                "quantity": product_quantity})
        return "Product successfully added to cart"

    def remove_from_cart(self, product_title):
        for i in range(len(self.cart_items)):
            if product_title == self.cart_items[i]["product_details"].title:
                self.cart_items.pop(i)
                return "Product successfully removed from cart"

    def change_cart_product_quantity(self, product_title, new_quantity):
        for product in self.cart_items:
            if product_title == product["product_details"].title:
                product["quantity"] = new_quantity
                return "Product quantity changed successfully"

    def view_cart(self):
        cart_str = ""
        for product in self.cart_items:
            cart_str += "{} Quantity: {} \n".format(product["product_details"], product["quantity"])
        cart_str += "total: {}".format(self.total_price())
        return cart_str

    def total_price(self):
        total = Money("USD", 0)
        for product in self.cart_items:
            total += prices[product["product_details"].title] * product["quantity"]
        return total

    def add_to_favourites(self, product_title):
        if len(self.favourite_products) == 0:
            self.favourite_products.append(Product(product_title, prices[product_title]))
        for product in self.favourite_products:
            if product_title != product.title:
                self.favourite_products.append(Product(product_title, prices[product_title]))
                break
        return "Product successfully added to favourites' list"

    def remove_from_favourites(self, product_title):
        for i in range(len(self.favourite_products)):
            if product_title == self.favourite_products[i].title:
                self.favourite_products.pop(i)
                return "Product successfully removed from favourites"

    def view_favourites(self):
        favourites_str = ""
        for product in self.favourite_products:
            favourites_str += "{}\n".format(product)
        return favourites_str

    def make_order(self, full_name, shipping_address, billing_account: BankAccount):
        purchase = Purchase(self.cart_items, full_name, shipping_address)
        self.purchase_history.append(purchase)
        company_account = BankAccount(CustomerData("Name", "Surname", Date(10, 1, 2000),
                                                   "example1@gmail.com", "password_1", "11111111",
                                                   "PN111111"), Date(12, 7, 2023), Time(11, 13, 0), "USD")

        billing_account.transfer_to_another_account(company_account, purchase.total_price, "EPOS PURCHASE")
        self.cart_items = 0
        return "Order placed successfully"

    def get_purchase_history(self):
        purchase_str = ""
        for purchase in self.purchase_history:
            purchase_str += "{}\n".format(purchase)
        return purchase_str

    def change_password(self):
        check_password = input("Enter your password: ")
        if check_password == self.__password:
            new_password = input("Enter new password: ")
            self.__password = new_password
            return "Password changed successfully"
        else:
            return "Wrong password, please try again"

    def change_email(self):
        check_password = input("Enter your password: ")
        if check_password == self.__password:
            new_email = input("Enter new email address: ")
            self.email = new_email
            return "Email changed successfully"
        else:
            return "Wrong password, please try again"

    def change_phone_number(self):
        check_password = input("Enter your password: ")
        if check_password == self.__password:
            new_phone_number = input("Enter new phone number: ")
            self.phone_number = new_phone_number
            return "Phone number changed successfully"
        else:
            return "Wrong password, please try again"


c = CustomerAccount("Ani", "Dilan", Date(20, 3, 2005), "anidilanyan05@gmail.com", "password_", "+37499333432")
c.add_to_cart("Apple", 2)
c.add_to_cart("Apple", 3)
c.add_to_cart("Banana", 2)
c.add_to_cart("Pear", 2)
c.change_cart_product_quantity("Apple", 2)
c.remove_from_cart("Apple")
# print(c.view_cart())
# c.add_to_favourites("Apple")
# c.add_to_favourites("Apple")
# c.add_to_favourites("Banana")
# c.add_to_favourites("Pear")
# c.remove_from_favourites("Apple")
# print(c.view_favourites())

# client_bank_account = BankAccount(
#     CustomerData("FN2", "LN2", Date(20, 2, 2000), "example2@gmail.com", "password_2", "222222222", "PN2222222"),
#     Date(12, 7, 2020), Time(11, 13, 0), "AMD")
# client_bank_account + Money("USD", 500)
#
# print(c.make_order("Ani Dilanyan", "Some Address", client_bank_account))
# print(client_bank_account.get_balance())
# print(c.get_purchase_history())

print(c.change_password())
