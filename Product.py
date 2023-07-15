from Money import Money
from MyExceptions import ProductTypeError, ProductValueError


class Product:
    def __init__(self, _id, title, price, quantity):
        try:
            if type(title) != str:
                raise ProductTypeError("product title", title)
            elif type(price) != Money:
                raise ProductTypeError("product price", price)
            elif type(_id) != int:
                raise ProductTypeError("id", id)
            elif type(quantity) != int:
                raise ProductTypeError("product quantity", quantity)

            if _id <= 0:
                raise ProductValueError("Unsupported negative value for id", _id)
            elif quantity < 0:
                raise ProductValueError("Unsupported negative value for product quantity", quantity)
        except (ProductTypeError, ProductValueError) as error:
            print(error)
        else:
            self.id = _id
            self.title = title
            self.price = price
            self.quantity = quantity

    def __repr__(self):
        try:
            return "Id:{} {} {} quantity:{}".format(self.id, self.title, self.price, self.quantity)
        except AttributeError:
            return "Object is empty"

    def buy(self, purchase_quantity):
        try:
            if type(purchase_quantity) != int:
                raise ProductTypeError("purchase quantity", purchase_quantity)

            if purchase_quantity > self.quantity:
                raise ProductValueError("No enough quantity in inventory", purchase_quantity)
            elif purchase_quantity < 0:
                raise ProductValueError("Unsupported negative value for purchase quantity", purchase_quantity)

        except (ProductValueError, ProductTypeError) as purchase_error:
            return purchase_error
        else:
            self.quantity -= purchase_quantity
            return "Purchase completed successfully"

    def change_quantity(self, new_quantity):
        try:
            if type(new_quantity) != int:
                raise ProductValueError("new quantity", new_quantity)
        except AttributeError:
            return "Attribute 'quantity' not found"
        except ProductValueError as err:
            return err
        else:
            self.quantity = new_quantity
            return "Quantity changed successfully"

    def __eq__(self, other):
        return self.id == other.id and self.title == other.title and self.price == other.price


# apple = Product(1, "Apple", Money("USD", 1), 10)
# pear = Product(2, "Pear", Money("USD", 2), 20)
# apple2 = Product(1, "Apple", Money("USD", 1), 10)
# print(apple.buy(5))
# print(apple == apple2)
