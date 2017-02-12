class Item:
    itemCount = 0

    def __init__(self, itemName):
        self.itemName = itemName
        self.sold = 0
        Item.itemCount += 1

    def displayCount(self):
        print "Total Employee %d" % Item.itemCount

    def displayEmployee(self):
        print "Item : ", self.itemName, ", QTY_sold: ", self.sold