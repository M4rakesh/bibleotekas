from prettytable import PrettyTable
table=PrettyTable()
table.field_names=["Name","Age","City"]
table.add_row(["Tom","15","Riga"])
print(table)