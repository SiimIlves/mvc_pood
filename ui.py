# ui.py

#import classes and files
from product import Product
from shop import Shop
from controller import Controller
from model import Model
from view import View
from shop import Shop

#create products
bread = Product("bread", 0.80, 10)
milk = Product("bread", 0.80, 10)
wine = Product("wine", 5.60, 5)

# create shop and add products to it
shop = Controller(Model(shop()), View())
shop.addProduct("bread", 0.80, 10)
shop.addProduct("bread", 0.80, 10)
shop.addProduct("wine", 5.60, 5)
# test shop content
for item in shop:
    print(item)