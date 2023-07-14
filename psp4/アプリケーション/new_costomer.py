import Table

table_list = [[]]



def ManageCostomerInformation(table_name, number_of_people, age):
    new = Table.Table(table_name, 0, number_of_people, age, 0)
    newninfo = new.Table_list()
    table_list[table_name][] = newinfo

ManageCostomerInformation(2, 4, 20)

print(table_list)