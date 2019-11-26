import csv

with open('cities.csv', 'r') as f:
    with open('new_cites.csv', 'w') as wf:
        writer = csv.writer(wf)
        reader = csv.DictReader(f)

        for row in reader:
            writer.writerow([row[' "City"'][2:-1], row[' "State"']])
