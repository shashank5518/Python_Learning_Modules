import csv

with open("csv_file", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    with ("new_csv_file", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="-")

        for line in csv_reader:
            csv_writer.writerow(line)

# csv.DictReader(file_alias)
# csv.DictWriter(file_alias, fieldnames=fieldnames, delimiter='')
# csv.writer.writeheader()
