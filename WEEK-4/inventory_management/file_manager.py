import csv
from food_item import *
from inventory import *
from datetime import datetime

# Function to save inventory to a CSV file
def save_items(inventory, filename='inventory.csv'):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Category', 'Quantity', 'Barcode', 'Expiry_date', 'Price'])
            for item in inventory.items:
                writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date.strftime('%Y-%m-%d'), item.price])
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

# Function to load inventory from a CSV file
def load_items(filename='inventory.csv'):
    items = Inventory()
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                items.add_item(FoodItem(
                    name=row['Name'],
                    category=row['Category'],
                    quantity=int(row['Quantity']),
                    barcode=row['Barcode'],
                    expiry_date=datetime.strptime(row['Expiry_date'], '%Y-%m-%d'),
                    price=float(row['Price'])
                ))
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred while loading from CSV: {e}")
    return items
