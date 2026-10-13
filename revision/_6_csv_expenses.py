import csv

with open('expenses_clean.csv', 'r') as expense_file:
    expenses = csv.DictReader(expense_file)

    for line in expenses:
        print(line['category'])