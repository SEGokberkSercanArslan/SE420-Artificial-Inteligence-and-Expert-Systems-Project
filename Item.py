
class Item:
    def __init__(self,type,quantity):
        self.type = type
        self.quantity = quantity

    def get_type(self):
        return self.type
    def get_quantity(self):
        return self.quantity
    def decrease_quantity(self,dec):
        self.quantity -= dec
    def increase_quantity(self,inc):
        self.quantity += inc