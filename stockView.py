class stockViews:
    # show items
    def showStocks(self, stockItems):
        print("Stock items")
        print("================================")
        print("---------------------------")
        print("name\t|\tprice\t|\tamount")
        for item in stockItems:
            if item.getAmount() == 0:
                pass
            if item.getAmount() > 0:
                print(item.getName() + "\t|\t" +
                    str(item.getPrice()) + "\t\t|\t" +
                    str(item.getAmount()))
                print("---------------------------")
        print("================================")

    # show item
    def showStock(self, item):
        print("Item -{}- in stock".format(item.getName()))
        print("============================")
        print("name\t|\tprice\t|\tamount")
        print(item.getName() + "\t|\t" +
              str(item.getPrice()) + "\t\t|\t" +
              str(item.getAmount()))
        print("============================")