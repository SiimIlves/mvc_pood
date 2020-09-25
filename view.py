class View:
    # show items
    def showItems(self, items):
        print("Shop items")
        print("============================")
        print("---------------------------")
        print("name\t|\tprice\t|\tamount")
        for item in items:
            print(item.getName()+"\t|\t"+
                  str(item.getPrice())+"\t\t|\t"+
                  str(item.getAmount()))
            print("---------------------------")
        print("============================")
        
    # show item
    def showItem(self, item):
        print("Item -{}-".format(item.getName()))
        print("============================")
        print("name\t|\tprice\t|\tamount")
        print(item.getName()+"\t|\t"+
                  str(item.getPrice())+"\t\t|\t"+
                  str(item.getAmount()))
        print("============================")

    # no item error
    def noItemError(self, name):
        print("============================")
        print("Shop is not selling {}.".format(name))
        print("============================")
        
    def remItem(self, name):
        print("Removing {}...".format(name))
        print("Removed {}!".format(name))
    
    def remAll(self):
        print("Removing everything.")
        
    def updItem(name):
        print("Updated {}.".format(name))
