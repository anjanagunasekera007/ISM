class Item:
   'Common base class for all employees'
   itemCount = 0

   def __init__(self, name):
      self.name = name
      self.soldQ1 = 0
      self.soldQ2 = 0
      self.soldQ3 = 0
      self.soldQ4 = 0
      self.itemc1 = 0
      self.itemc2 = 0
      self.itemc3 = 0
      self.itemc4 = 0
      self.itemc5 = 0
      self.itemc6 = 0
      self.itemc7 = 0
      self.soldTotal = 0
      Item.itemCount += 1

class FullItem:
   'Common base class for all employees'
   itemCount = 0

   def __init__(self, id, name,description,categoryname,category,price,instock,inshelf,orderQty,weight):
      self.id = id
      self.name = name
      self.description = description
      self.categoryname = categoryname
      self.category = category
      self.soldQ1 = 0
      self.soldQ2 = 0
      self.soldQ3 = 0
      self.soldQ4 = 0
      self.soldTotal = 0
      self.price = price
      self.instock = instock
      self.inshelf = inshelf
      self.orderQty = orderQty
      self.weight = weight
      self.shelfcapacity = 50


      Item.itemCount += 1


class Item:
   'Common base class for all employees'
   itemCount = 0

   def __init__(self, id, name,description,category):
      self.id = id
      self.name = name
      self.description = description
      self.category = category
      self.soldQ1 = 0
      self.soldQ2 = 0
      self.soldQ3 = 0
      self.soldQ4 = 0
      self.itemc1 = 0
      self.itemc2 = 0
      self.itemc3 = 0
      self.itemc4 = 0
      self.itemc5 = 0
      self.itemc6 = 0
      self.itemc7 = 0
      self.soldTotal = 0
      Item.itemCount += 1

