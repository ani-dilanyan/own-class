from datetime import datetime
from Money import Money


class Purchase:
    def __init__(self, products, full_name, shipping_address):
        self.products = products
        self.fullname = full_name
        self.shipping_address = shipping_address

        self.purchase_date_time = "{}:{} {}".format(datetime.now().hour, datetime.now().minute, datetime.now().date())

        total = Money("USD", 0)
        for product in products:
            total += product.price * product.quantity
        self.total_price = total

    def __repr__(self):
        products_str = ""
        for product in self.products:
            products_str += "{}\n".format(product)

        return "Products:\n{}Total:{}\nPurchased on: {}\nShipping address: {}".format(products_str,
                                                                                      self.total_price,
                                                                                      self.purchase_date_time,
                                                                                      self.shipping_address)
