from Money import Money
from Product import Product
from MyExceptions import ProductValueError, ProductTypeError


class Inventory:
    def __init__(self, products=[]):
        try:
            if type(products) != list:
                raise ProductTypeError("product list", products)

            for product in products:
                if type(product) != Product:
                    raise ProductTypeError("product", product)

        except ProductTypeError as err:
            print(err)
        else:
            self.products = products

    def __repr__(self):
        try:
            inventory_str = ""
            for product in self.products:
                inventory_str += "{}\n".format(product)
            return inventory_str
        except AttributeError:
            return "Object is empty. Inventory setup is incomplete"

    def add_product(self, product: Product):
        try:
            if type(product) != Product:
                raise ProductTypeError("product to add", product)
            if product in self.products:
                raise ProductValueError("product is already in inventory", product)
        except (ProductTypeError, ProductValueError) as error:
            return error
        else:
            self.products.append(product)
            return "Product added successfully"

    def remove_product(self, product: Product):
        try:
            if type(product) != Product:
                raise ProductTypeError("product to remove", product)

            if product not in self.products:
                raise ProductValueError("There is no such product in inventory", product)
        except ProductTypeError as error:
            return error
        else:
            self.products.remove(product)
            return "Product removed successfully"

    def sum_of_products(self):
        total = Money("USD", 0)
        for product in self.products:
            total += product.price * product.quantity
        return total

    def get_inventory_product_titles(self):
        return [product.title for product in self.products]

    def get_inventory_product_prices(self):
        return [product.title for product in self.products]

    def get_inventory_product_quantity(self):
        return [product.quantity for product in self.products]

    def get_inventory_product_id(self):
        return [product.id for product in self.products]

# apple = Product(1, "Apple", Money("USD", 1), 10)
# pear = Product(2, "Pear", Money("USD", 2), 20)
# blueberry = Product(3, "Blueberry", Money("USD", 3), 30)
# c = Inventory([apple, pear])
# print(c)
# print(c.add_product(blueberry))
# print(c)
# print(c.remove_product(pear))
# print(c)
# print(c.sum_of_products())
