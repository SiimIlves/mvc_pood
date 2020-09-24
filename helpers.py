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

def remItem():
    import sys
    global items
    ask1 = input("Would you like to remove anything? (yes/no) ")
    if ask1 == "No" or ask1 == "no":
        print("Understandable, have a great day.")
        return
    if ask1 == "Yes" or ask1 == "yes":
        remove = input("What would you like to remove? ")
        for item in items:
            if remove == item.getName():
                print("item found!")
                items.remove(item)
                break
            if remove != item:
                print("Looking...")
        ask2 = input("Would you like to remove anything else? (yes/no) ")
        if ask2 == "no" or ask2 == "No":
            print("Understandable, have a great day.")
            return
        if ask2 == "yes" or ask2 == "Yes":
            remove = input("What would you like to remove? ")
            for item in items:
                if remove == item.getName():
                    print("item found!")
                    items.remove(item)
                    break
                if remove != item:
                    print("Looking...")
        while ask2 == "yes" or "Yes":
            ask2 = input("Would you like to remove anything else? (yes/no) ")
            if ask2 == "no" or ask2 == "No":
                print("Understandable, have a great day.")
                return
            if ask2 == "yes" or ask2 == "Yes":
                remove = input("What would you like to remove? ")
                for item in items:
                    if remove == item.getName():
                        print("item found!")
                        items.remove(item)
                        break
                    if remove != item:
                        print("Looking...")

def updItem():
    global items
    ask = input("Would you like to update any of the items? (yes/no) ")
    if ask == "No" or ask == "no":
        print("Understandable, have a great day.")
    if ask == "Yes" or ask == "yes":
        update = input("What would you like to update? ")
        for item in items:
            if update == item.getName():
                print("What would you like to update about it?")
                what = input("Name, price, amount? ")
                if what == "name" or what == "Name":
                    newName = input("Enter a new name: ")
                    item.setName(newName)
                if what == "price" or what == "Price":
                    newPrice = input("Enter a new price: ")
                    item.setPrice(newPrice)
                if what == "amount" or what == "Amount":
                    newAmount = input("Enter a new amount: ")
                    item.setAmount(newAmount)
                what2 = input("Anything else? ")
                while what2 == "yes" or what2 == "Yes":
                    if what2 == "no" or what2 == "No":
                        break
                    what = input("Name, price, amount? ")
                    if what == "name" or what == "Name":
                        newName = input("Enter a new name: ")
                        item.setName(newName)
                    if what == "price" or what == "Price":
                        newPrice = input("Enter a new price: ")
                        item.setPrice(newPrice)
                    if what == "amount" or what == "Amount":
                        newAmount = input("Enter a new amount: ")
                        item.setAmount(newAmount)
                    what2 = input("Anything else? ")

def remAll():
    global items
    items.clear()
    
# show item
def showItem(name):
    global items
    # control all items step by step
    for item in items:
        # if the name is the same as we search
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("Couldn't find {}!".format(name))
