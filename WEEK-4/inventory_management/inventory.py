import csv
from datetime import datetime


#-------------------Inventory Class-------------------
# this class is used to manage the inventory
class Inventory:
    def __init__(self):
        self.items = []

    def __iter__(self):
        return iter(self.items)

    def near_expiry_generator(self, days=7):
        current_date = datetime.now().date()
        for item in self.items:
            expiry_date = datetime.strptime(item.expiry_date, '%Y-%m-%d').date()
            if (expiry_date - current_date).days <= days:
                yield item

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
    
    def search_item(self, keyword):
        results = [item for item in self.items if keyword.lower() in item.name.lower() or keyword in item.barcode]
        if results:
            for item in results:
                print(item)
        else:
            print("No items found.")
    

    # this function is used to search for an item in the inventory by expiry date
    def near_expiry_items(self, days=7):
        near_expiry = []
        current_date = datetime.now().date()
        for item in self.items:
            expiry_date = datetime.strptime(item.expiry_date, '%Y-%m-%d').date()
            if (expiry_date - current_date).days <= days:
                near_expiry.append(item)
        return near_expiry
