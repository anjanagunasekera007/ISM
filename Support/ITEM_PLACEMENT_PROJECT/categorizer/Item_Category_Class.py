class ItemC:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, category, categoryid):
        self.name = name
        self.category = category
        self.categoryid = categoryid
