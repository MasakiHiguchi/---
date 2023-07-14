class Table:
    def __init__(self, table_name, bashing_status, number_of_people, age, total_amount):
        self.table_name = table_name
        self.bashing_status = 0
        self.number_of_people = number_of_people
        self.age = age
        self.total_amount = total_amount

        def ReleaceBashingStatus(self):
            self.bashing_status = 0

Table_list = []
Table_name = 1
for i in range(4):
    Table_list.append(Table_name)
    Table_name = Table_name + 1
