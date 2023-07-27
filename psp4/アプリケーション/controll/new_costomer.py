from entity.Table import Table

def new_customer():
    table = input("Enter table name (T１, T２, T３): ")
    name = input("Enter customer name: ")
    bashing_status = input("Enter bashing status (1 for Yes, 0 for No): ").strip() == "1"
    number_of_people = int(input("Enter number of people: "))
    age = int(input("Enter customer's age: "))
    total_amount = float(input("Enter total amount: "))

    return Table(table=table,
                 name=name,
                 bashing_status=bashing_status,
                 number_of_people=number_of_people,
                 age=age,
                 total_amount=total_amount)

if __name__ == "__main__":
    Tables = [[], [], []]  # 二次元リストの初期化

    while True:
        table_instance = new_customer()
        
        if table_instance.table == "T１":
            Tables[0].append(table_instance)
        elif table_instance.table == "T２":
            Tables[1].append(table_instance)
        elif table_instance.table == "T３":
            Tables[2].append(table_instance)
        else:
            print("Invalid table name. Please enter T１, T２, or T３.")
        
        continue_input = input("Do you want to add another customer? (y/n): ")
        if continue_input.lower() != "y":
            break

    # Tablesに格納されたデータを表示
    for i, table_list in enumerate(Tables, start=1):
        print(f"--- Table T{i} ---")
        for customer in table_list:
            print("Table:", customer.table)
            print("Name:", customer.name)
            print("Bashing Status:", customer.bashing_status)
            print("Number of People:", customer.number_of_people)
            print("Age:", customer.age)
            print("Total Amount:", customer.total_amount)
            print()
