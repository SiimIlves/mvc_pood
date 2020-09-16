import exceptions

# represents shop structure
# list of Product type objects
items = []

# add item to items
def addItem(name, price, amount):
    global items
    # create product with required description
    product = Product(name, price, amount)
    # control if item already exists
    if product in items:
        raise exceptions.ItemExists("Item {} exists.".format(name))
    else:
        items.append(product)