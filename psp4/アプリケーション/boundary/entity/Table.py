class Table:
    def __init__(self, table, name, bashing_status, number_of_people, age, total_amount):
        valid_tables = ["T１", "T２", "T３"]
        if table not in valid_tables:
            raise ValueError("Invalid table name. Allowed values are T１, T２, T３.")
        
        self.table = table
        self.name = name
        self.bashing_status = 1 if bashing_status else 0
        self.number_of_people = number_of_people
        self.age = age
        self.total_amount = total_amount
