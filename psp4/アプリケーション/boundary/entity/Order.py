class Order:
    def __init__(self, table_name, quantity, total_amount):
        self.table_name = table_name
        self.quantity = quantity
        self.total_amount = total_amount

    def __str__(self):
        return f"Table: {self.table_name}, Quantity: {self.quantity}, Total Amount: ${self.total_amount}"