import csv
from food_item import *

def load_items(file_name):
    items = []
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    item = FoodItem(row[0], row[1], int(row[2]), row[3], row[4])
                    items.append(item)
    except FileNotFoundError:
        print("File not found. Starting with an empty inventory.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return items

def save_items(file_name, items):
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for item in items:
                writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date])
    except Exception as e:
        print(f"Error writing to file: {e}")
