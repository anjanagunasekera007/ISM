class Item:
   'Common base class for all employees'
   itemCount = 0

   def __init__(self, id, name,description,categoryname,category,price,instock,inshelf,shelfcapacity,weight,url,suppliername,supplieraddress,supplisercontactnumber):
      self.id = id
      self.name = name
      self.description = description
      self.categoryname = categoryname
      self.category = category
      self.price = price
      self.instock = instock
      self.inshelf = inshelf
      self.shelfcapacity = shelfcapacity
      self.weight = weight
      self.url = url
      self.suppliername = suppliername
      self.supplieraddress = supplieraddress
      self.suppliercontactnumber = supplisercontactnumber

      self.soldQ1 = 0
      self.soldQ2 = 0
      self.soldQ3 = 0
      self.soldQ4 = 0
      self.soldTotal = 0



