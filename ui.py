# ui.py

# import classes and files
from product import Product
from shop import Shop
from controller import Controller
from model import Model
from model_stock import ModelStock
from view import View
from stock import Stock
from stockView import stockViews

# create shop and add products to shop
shop = Controller(Model(Shop()), View())
stock = Controller(ModelStock(Stock()), stockViews())
stock.addItem("bread", 0.80, 10)
stock.addItem("popcorn", 0.5, 50)
stock.addItem("car", 12000.0, 1)

# already in shop
shop.addItem("bread", 0.80, 10)
shop.addItem("milk", 0.50, 30)

# stock market
shop.restock("car", 12000.0, 1)
shop.showItems()
stock.showStocks()