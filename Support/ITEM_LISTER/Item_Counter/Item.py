class Item:
    'Common base class for all employees'
    itemcounter = 0

    def __init__(self, name):
        self.name = name
        self.sold = 0
        Item.itemcounter += 1

    # def displayCount(self):
    #     print "Total Employee %d" % Employee.empCount
    #
    # def displayEmployee(self):
    #     print "Name : ", self.name, ", Salary: ", self.salary

    def display(self):
        print "OK"