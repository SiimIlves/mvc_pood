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

    def remItem(self):
        items = self.model.remItem()

    def updItem(self):
        items = self.model.updItem()

    def remAll(self):
        items = self.model.remAll()
