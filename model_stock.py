import helpers_stock

class ModelStock:
    # get shop data - [] of products
    def __init__(self, stockItems):
        self.stockItems = stockItems
    # add item to items
    def addItem(self, name, price, amount):
        helpers_stock.addItem(name, price, amount)
    # show item
    def showItems(self):
        return helpers_stock.showItems()
    def remItem(self, name):
        helpers_stock.remItem(name)
    def updItem(self, name, price, amount):
        helpers_stock.updItem(name, price, amount)
    def remAll(self):
        helpers_stock.remAll()
    def showItem(self, name):
        return helpers_stock.showItem(name)