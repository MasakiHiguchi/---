from Table import Table

class Total:
    def __init__(self, table_name, total_amount, deposit_amount, change):
        self.table = Table(table_name, 0, 0)  # Tableクラスのインスタンスを生成
        self.total_amount = total_amount
        self.deposit_amount = deposit_amount
        self.change = change

    def __str__(self):
        return f"Table: {self.table.name}, Total Amount: ${self.total_amount}, Deposit: ${self.deposit_amount}, Change: ${self.change}"
