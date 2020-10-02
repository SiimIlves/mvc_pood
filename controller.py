import exceptions
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def addItem(self, name, price, amount):
        try:
            self.model.addItem(name, price, amount)
            print("OK")
        except:
            print("No")

    def showItems(self):
        items = self.model.showItems()
        self.view.showItems(items)

    def showStocks(self):
        stockItems = self.model.showStocks()
        self.view.showStocks(stockItems)

    def remItem(self, name):
        try:
            self.model.remItem(name)
            self.view.remItem(name)
        except:
            pass
        
    def updItem(self, name, price, amount):
        try:
            self.model.updItem(name, price, amount)
            self.view.updItem(name)
            self.showItems(name)
        except:
            print("")

    def remAll(self):
        items = self.model.remAll()

    def showItem(self, name):
        try:
            item = self.model.showItem(name)
            self.view.showItem(item)
        except:
            self.view.noItemError(name)

    def restock(self, name, price, amount):
        try:
            self.model.restock(name, price, amount)
            print("OK")
        except:
            print("No")