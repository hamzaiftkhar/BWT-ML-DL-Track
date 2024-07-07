from inventory import *
from food_item import *
from file_manager import *
from datetime import datetime

FILE_NAME = 'inventory.csv'

def display_menu():
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Edit Item")
    print("3. Delete Item")
    print("4. Search Item")
    print("5. List All Items")
    print("6. Save & Exit")
    print("7. Exit without Saving")

def add_item(inventory):
    name = input("Enter item name: ")
    category = input("Enter item category: ")
    quantity = int(input("Enter item quantity: "))
    barcode = input("Enter item barcode: ")
    expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
    price = float(input("Enter item price: "))
    item = FoodItem(name, category, quantity, barcode, expiry_date, price)
    inventory.add_item(item)

def edit_item(inventory):
    barcode = input("Enter the barcode of the item to edit: ")
    name = input("Enter new name (leave blank to keep unchanged): ")
    category = input("Enter new category (leave blank to keep unchanged): ")
    quantity = input("Enter new quantity (leave blank to keep unchanged): ")
    expiry_date = input("Enter new expiry date (YYYY-MM-DD) (leave blank to keep unchanged): ")
    price = input("Enter new price (leave blank to keep unchanged): ")
    kwargs = {}
    if name:
        kwargs['name'] = name
    if category:
        kwargs['category'] = category
    if quantity:
        kwargs['quantity'] = int(quantity)
    if expiry_date:
        kwargs['expiry_date'] = expiry_date
    if price:
        kwargs['price'] = float(price)
    inventory.edit_item(barcode, **kwargs)

def delete_item(inventory):
    barcode = input("Enter the barcode of the item to delete: ")
    inventory.delete_item(barcode)

def search_item(inventory):
    keyword = input("Enter the barcode or name to search: ")
    inventory.search_item(keyword)

def list_all_items(inventory):
    for item in inventory:
        print(item)

def main():
    inventory = Inventory()
    inventory.items = load_items(FILE_NAME)

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            edit_item(inventory)
        elif choice == '3':
            delete_item(inventory)
        elif choice == '4':
            search_item(inventory)
        elif choice == '5':
            list_all_items(inventory)
        elif choice == '6':
            save_items(FILE_NAME, inventory.items)
            print("Inventory saved. Exiting...")
            break
        elif choice == '7':
            print("Exiting without saving...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
