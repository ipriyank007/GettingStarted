import csv

with open('csv_files/HES2018-Table5.csv', 'r') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        # del row['Year']
        print(row['Year'])
