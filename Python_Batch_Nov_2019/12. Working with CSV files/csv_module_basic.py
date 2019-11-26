import csv

with open('demo.csv', 'r') as f:
    with open('sample.csv', 'w') as wf:
        csv_reader = csv.reader(f, delimiter='\t')
        csv_writer = csv.writer(wf, delimiter='-')

        for row in csv_reader:
            csv_writer.writerow(row)
        
        

# with open('demo.tsv', 'r') as f:
#     csv_reader = csv.reader(f, delimiter='\t')

#     for row in csv_reader:
#         print(row)
