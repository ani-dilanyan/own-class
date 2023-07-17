import datetime
from Money import Money
from Person import Person
from Product import Product
from MyExceptions import CustomerDataTypeError, CustomerDataValueError, ProductTypeError, ProductValueError, \
    PersonalDataTypeError
from Date import Date
from Time import Time
from Purchase import Purchase
from Bank_account import BankAccount
from CustomerData import CustomerData
from ShopInventory import inventory


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

    def add_to_cart(self, product):
        try:
            if type(product) != Product:
                raise ProductTypeError("product", product)
            for product_in_inventory in inventory.products:
                if product.id == product_in_inventory.id and product.quantity > product_in_inventory.quantity:
                    raise ProductValueError("No enough {} in the inventory".format(product.title), product.quantity)
        except (ProductTypeError, ProductValueError) as err:
            return err
        except AttributeError:
            return "Attribute 'cart_items' not found"
        else:
            for product_in_cart in self.cart_items:
                if product == product_in_cart:
                    product_in_cart.quantity += product.quantity
                    return "Product successfully added to cart"

            self.cart_items.append(product)
            return "Product successfully added to cart"

    def remove_from_cart(self, product_index):
        try:
            if type(product_index) != int:
                raise ProductTypeError("product title", product_index)
            if product_index > len(self.cart_items):
                raise ProductValueError("product index", product_index)
        except ProductTypeError as err:
            return err
        except AttributeError:
            return "Attribute 'cart_items' not found"
        else:
            self.cart_items.pop(product_index)
            return "Product successfully removed from cart"

    def change_cart_product_quantity(self, product_index, new_quantity):
        try:
            if type(product_index) != int:
                raise ProductTypeError("product title", product_index)
            if product_index > len(self.cart_items):
                raise ProductValueError("product index", product_index)
        except ProductTypeError as err:
            return err
        except AttributeError:
            return "Attribute 'cart_items' not found"
        else:
            self.cart_items[product_index].change_quantity(new_quantity)
            return "Product quantity changed successfully"

    def view_cart(self):
        cart_str = ""
        if self.cart_items:
            for product in self.cart_items:
                cart_str += "{}\n".format(product)
            cart_str += "total: {}".format(self.total_price())
        else:
            cart_str = "No products to show"
        return cart_str

    def total_price(self):
        total = Money("USD", 0)
        for product in self.cart_items:
            total += product.price * product.quantity
        return total

    def add_to_favourites(self, product):
        try:
            if type(product) != Product:
                raise ProductTypeError("product", product)
        except ProductTypeError as err:
            return err
        except AttributeError:
            return "Attribute 'cart_items' not found"
        else:
            if len(self.favourite_products) == 0:
                self.favourite_products.append(product)
            for product_in_inventory in self.favourite_products:
                if product.title != product_in_inventory.title:
                    self.favourite_products.append(product)
                    break
            return "Product successfully added to favourites' list"

    def remove_from_favourites(self, product_index):
        try:
            if type(product_index) != int:
                raise ProductTypeError("product title", product_index)
            if product_index > len(self.favourite_products):
                raise ProductValueError("product index", product_index)
        except ProductTypeError as err:
            return err
        except AttributeError:
            return "Attribute 'cart_items' not found"
        else:
            self.favourite_products.pop(product_index)
            return "Product successfully removed from favourites"

    def view_favourites(self):
        favourites_str = ""
        for product in self.favourite_products:
            favourites_str += "{}\n".format(product)
        return favourites_str

    def make_order(self, full_name, shipping_address, billing_account: BankAccount):
        try:
            if type(full_name) != str:
                raise PersonalDataTypeError("full name", full_name)
            elif type(shipping_address) != str:
                raise PersonalDataTypeError("shipping_address", shipping_address)
            elif type(billing_account) != BankAccount:
                raise PersonalDataTypeError("billing account", billing_account)
        except AttributeError:
            return "Missing attribute 'cart_items'"
        else:
            purchase = Purchase(self.cart_items, full_name, shipping_address)
            company_account = BankAccount(CustomerData("Name", "Surname", Date(10, 1, 2000),
                                                       "example1@gmail.com", "password_1", "11111111",
                                                       "PN111111"), Date(12, 7, 2023), Time(11, 13, 0), "USD")

            billing_account.transfer_to_another_account(company_account, purchase.total_price, "EPOS PURCHASE")
            self.cart_items = 0
            self.purchase_history.append(purchase)
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


# c = CustomerAccount("Ani", "Dilan", Date(20, 3, 2005), "anidilanyan05@gmail.com", "password_", "+37499333432")
# print(c.add_to_cart(Product(1, "Apple", Money("USD", 1), 3)))
# c.add_to_cart(Product(2, "Pear", Money("USD", 2), 2))
# c.add_to_cart(Product(2, "Pear", Money("USD", 2), 8))
# c.change_cart_product_quantity(0, 2)
# c.remove_from_cart(0)
# print(c.view_cart())

# c.add_to_favourites(Product(1, "Apple", Money("USD", 1), 1))
# c.add_to_favourites(Product(2, "Pear", Money("USD", 2), 2))
# c.remove_from_favourites(0)
# print(c.view_favourites())

# client_bank_account = BankAccount(
#     CustomerData("FN2", "LN2", Date(20, 2, 2000), "example2@gmail.com", "password_2", "222222222", "PN2222222"),
#     Date(12, 7, 2020), Time(11, 13, 0), "AMD")
# client_bank_account + Money("USD", 500)
#
# print(c.make_order("Ani Dilanyan", "Some Address", client_bank_account))
# print(client_bank_account.get_balance())
# print(c.get_purchase_history())

# print(c.change_password())
