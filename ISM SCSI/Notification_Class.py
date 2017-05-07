class ReOrderNotification:
   def __init__(self, id,notification,ITEMQty,date,status):
      self.id = id
      self.notification = notification
      self.ITEMQty = ITEMQty
      self.date = date
      self.status = status

class ReStockNotification:
   def __init__(self, id,notification,OrderQTY,orderdate,deliverydate,status):
      self.id = id
      self.notification = notification
      self.ITEMQty = OrderQTY
      self.orderdate = orderdate
      self.date = deliverydate
      self.status = status
