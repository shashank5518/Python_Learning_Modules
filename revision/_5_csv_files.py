import csv

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)

    # next(csv_reader)

    with open('new_names.csv', 'w') as new_file:
        field_names = ['first_name', 'last_name', 'email']
        # csv_writer = csv.writer(new_file, delimiter = '-')
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter = '\t')
        
        csv_writer.writeheader()

        for line in csv_reader:
            # print(line)
            # print(line[2])
            # del line['email']
            csv_writer.writerow(line)