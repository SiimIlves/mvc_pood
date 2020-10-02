import exceptions
from product import Product

# represents shop structure
# list of Product type objects
items = []

# add item to items
def addItem(name, price, amount):
    global items
    # create product with required description
    product = Product(name, price, amount)
    # control is item already exists
    if product in items:
        raise exceptions.ItemExists("Item {} exists".format(name))
    else:
        items.append(product)
# show items
def showItems():
    global items
    # control if items exists
    if len(items) == 0:
        raise exceptions.ItemExists("List of items is empty")
    else:
        return items

def remItem(name):
    import sys
    global items
    for item in items:
        if name == item.getName():
            items.remove(item)
        else:
            continue
    if name not in items:
        raise exceptions.ItemDoesntExist("-{}- does not exist!".format(name))

def updItem(name, price, amount):
    global items
    for item in items:
        if item.getName() == name:
            item.setPrice(price)
            item.setAmount(amount)
        else:
            continue
            raise exceptions.ItemDoesntExist("Couldn't update {}, because it doesn't exist.".format(name))

def remAll():
    global items
    items.clear()
    
# show item
def showItem(name):
    global items
    for item in items:
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("Couldn't find {}!".format(name))

def stack(name, price, takeAmount):
    global items
    global stockItems
    for item in stockItems:
        if(item.getName() == name):
            newAmount = (item.getAmount() - takeAmount)
            item.setAmount(newAmount)
            continue
        else:
            continue
            raise exceptions.ItemNotExists("Couldn't find {}.".format(name))

    for banana in items:
        # if the name matches our search
        if (banana.getName() == name):
            totalAmount = banana.getAmount() + takeAmount
            banana.setAmount(totalAmount)
            break
        else:
            product = Product(name, price, takeAmount)
            if product in items:
                print("{} already exists!".format(name))
            else:
                items.append(product)
            break
