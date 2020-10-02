import helpers
import helpers_stock

items = []
stockItems = []

class Model:
    # get shop data - [] of products
    def __init__(self, items):
        self.items = items
    # add item to items
    def addItem(self, name, price, amount):
        helpers.addItem(name, price, amount)
    # show item
    def showItems(self):
        return helpers.showItems()
    def remItem(self, name):
        helpers.remItem(name)
    def updItem(self, name, price, amount):
        helpers.updItem(name, price, amount)
    def remAll(self):
        helpers.remAll()
    def showItem(self, name):
        return helpers.showItem(name)
    def stock(self):
        return helpers.stock()
    def restock(self, name, price, amount):
        helpers.addItem(name, price, amount)
        helpers_stock.stock(name, price, amount)