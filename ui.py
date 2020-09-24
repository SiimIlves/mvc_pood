# ui.py

# import classes and files
from product import Product
from shop import Shop
from controller import Controller
from model import Model
from view import View

# create shop and add products to shop
shop = Controller(Model(Shop()), View())
shop.addItem("bread", 0.80, 10)
shop.addItem("milk", 0.50, 50)
shop.addItem("wine", 5.60, 5)
shop.addItem("popcorn", 3.9, 25)
shop.addItem("vodka", 4.0, 70)

# show item
shop.showItems()
shop.remItem()
shop.showItems()
