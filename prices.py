from Money import Money
from Inventory import Inventory
from Product import Product

prices = {
    "Apple": Money("USD", 25),
    "Pear": Money("USD", 20),
    "Banana": Money("USD", 23)
}

inventory = Inventory([
    Product(1, "Apple", Money("USD", 1), 10),
    Product(2, "Pear", Money("USD", 2), 20),
    Product(3, "Banana", Money("USD", 3), 30)
])
