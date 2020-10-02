import exceptions
from product import Product

# represents shop structure
# list of Product type objects
stockItems = []


# add item to stockItems
def addItem(name, price, amount):
    global stockItems
    # create product with required description
    product = Product(name, price, amount)
    # control is item already exists
    if product in stockItems:
        raise exceptions.ItemExists("Item {} exists".format(name))
    else:
        stockItems.append(product)


# show stockItems
def showStocks():
    global stockItems
    # control if stockItems exists
    if len(stockItems) == 0:
        raise exceptions.ItemExists("List of stockItems is empty")
    else:
        return stockItems


def remItem(name):
    import sys
    global stockItems
    for item in stockItems:
        if name == item.getName():
            stockItems.remove(item)
        else:
            continue
    if name not in stockItems:
        raise exceptions.ItemDoesntExist("-{}- does not exist!".format(name))


def updItem(name, price, amount):
    global stockItems
    for item in stockItems:
        if item.getName() == name:
            item.setPrice(price)
            item.setAmount(amount)
        else:
            continue
            raise exceptions.ItemDoesntExist("Couldn't update {}, because it doesn't exist.".format(name))


def remAll():
    global stockItems
    stockItems.clear()


# show item
def showItem(name):
    global stockItems
    for item in stockItems:
        if (item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("Couldn't find {}!".format(name))


def stock(name, price, amount):
    global stockItems
    for item in stockItems:
        if (item.getName() == name):
            aamount = item.getAmount()
            item.amount = item.setAmount(aamount - amount)
        else:
            continue
            raise exceptions.ItemExists("Can't add {} to shop.".format(name))