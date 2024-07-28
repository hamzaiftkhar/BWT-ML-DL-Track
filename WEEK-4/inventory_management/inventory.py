from datetime import date, datetime
from food_item import *

class Inventory:
    def __init__(self):
        self.items = []


    def add_item(self, item):
        self.items.append(item)

    def edit_item(self, barcode, **kwargs):
        for item in self.items:
            if item.barcode == barcode:
                for key, value in kwargs.items():
                    setattr(item, key, value)
                print(f"Item with barcode {barcode} has been updated.")
                return
        print("Item not found.")

    def delete_item(self, barcode):
        self.items = [item for item in self.items if item.barcode != barcode]
        print(f"Item with barcode {barcode} has been deleted.")

    def search_item(self, keyword):
        results = [item for item in self.items if keyword.lower() in item.name.lower() or keyword in item.barcode]
        if results:
            for item in results:
                print(item)
        else:
            print("No items found.")

     # Get food items that are near their expiry date
    def near_expiry_items(self, days_threshold=7):
        today = datetime.now()
        near_expiry_items = [item for item in self.items if (item.expiry_date - today).days <= days_threshold]
        return near_expiry_items

    def __iter__(self):
        return iter(self.items)

    def near_expiry_generator(self, days=7):
        current_date = date.today()
        for item in self.items:
            expiry_date = item.expiry_date
            if isinstance(expiry_date, str):
                expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').date()
            if (expiry_date - current_date).days <= days:
                yield item

    def generate_report(self):
        report = {
            "total_items": len(self.items),
            "near_expiry": len(list(self.near_expiry_generator())),
            "categories": {}
        }
        for item in self.items:
            if item.category not in report["categories"]:
                report["categories"][item.category] = 0
            report["categories"][item.category] += 1
        return report
