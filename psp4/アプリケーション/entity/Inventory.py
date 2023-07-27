# Inventory.py

class Inventory:
    def __init__(self, name, kind, quantity, price):
        self.name = name
        self.kind = kind
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.kind}) - Quantity: {self.quantity}, Price: ${self.price}"

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def update_price(self, new_price):
        self.price = new_price

