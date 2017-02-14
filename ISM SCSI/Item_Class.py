class Item:
   'Common base class for all employees'
   itemCount = 0

   def __init__(self, name):
      self.name = name
      self.soldQ1 = 0
      self.soldQ2 = 0
      self.soldQ3 = 0
      self.soldTotal = 0
      Item.itemCount += 1