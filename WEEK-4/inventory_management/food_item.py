#-------------------Food Item Class-------------------

class FoodItem:
    # this function is the constructor
    def __init__(self, name,category, quantity, barcode, expiry_date,  price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.barcode = barcode
        self.expiry_date = expiry_date
        self.price = price
    # this function is used to print the object
    def __str__(self):
        return f"{self.name} ({self.category}) - {self.quantity} units  -  Price: {self.price} - Expires on: {self.expiry_date}"

