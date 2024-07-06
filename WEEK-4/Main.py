#-------------------------------------------Stage-1-------------------------------------------

from datetime import datetime


#-------------------Food Item Class-------------------
class FoodItem:
    # this function is the constructor
    def __init__(self, name,category, quantity, barcode, expiry_date,  price):
        self.name = name
        self.price = category
        self.quantity = quantity
        self.barcode = barcode
        self.expiry_date = expiry_date
        self.price = price
    # this function is used to print the object
    def __str__(self):
        return f"{self.name} ({self.category}) - {self.quantity} units  -  Price: {self.price} - Expires on: {self.expiry_date}"


#-------------------Inventory Class-------------------
class Inventory:
    def __init__(self):
        self.items = []

    # this function is used to add an item to the inventory
    def add_item(self, item):
        self.items.append(item)

    # this function is used to print all the items in the inventory
    def edit_item(self, barcode, **kwargs):
        for item in self.items:
            if item.barcode == barcode:
                for key, value in kwargs.items():
                    setattr(item, key, value)
                return
        print("Item not found")

    # this function is used to delete an item from the inventory
    def delete_item(self, barcode):
        self.items = [item for item in self.items if item.barcode != barcode]

    # this function is used to search for an item in the inventory
    def search_item(self, barcode):
        for item in self.items:
            if item.barcode == barcode:
                return item
        return None
    
    # this function is used to search for an item in the inventory by category
    def search_by_category(self, category):
        return [item for item in self.items if item.category == category]
    
    # this function is used to search for an item in the inventory by name
    def search_by_name(self, name):
        return [item for item in self.items if item.name == name]

    # this function is used to search for an item in the inventory by expiry date
    def near_expiry_items(self, days=7):
        near_expiry = []
        current_date = datetime.now().date()
        for item in self.items:
            expiry_date = datetime.strptime(item.expiry_date, '%Y-%m-%d').date()
            if (expiry_date - current_date).days <= days:
                near_expiry.append(item)
        return near_expiry
