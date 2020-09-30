# ui.py

# import classes and files
from product import Product
from shop import Shop
from controller import Controller
from model import Model
from model_stock import ModelStock
from view import View
from stock import Stock

# create shop and add products to shop
shop = Controller(Model(Shop()), View())
stock = Controller(ModelStock(Stock()), View())
stock.addItem("bread", 0.80, 10)
stock.addItem("milk", 0.5, 50)

# already in shop
shop.addItem("bread", 0.80, 10)
shop.addItem("milk", 0.50, 30)
shop.addItem("car", 12000.0, 1)

# stock market
shop.restock("milk", 0.5, 49)
shop.showItems()
stock.showItems()