class Table:
    def __init__(self, table_name, bashing_status, number_of_people, age, total_amount):
        self.table_name = table_name
        self.bashing_status = 0
        self.number_of_people = number_of_people
        self.age = age
        self.total_amount = total_amount

    def ReleaceBashingStatus(self):
        self.bashing_status = 0

    def Table_list(self):
        list1=[self.table_name, self.bashing_status, self.number_of_people, self.total_amount]


table_list = [[]]
tables = 4
for i in range(tables):
    table_list.append(Table_name)
    Table_name = Table_name + 1

print(table_list)