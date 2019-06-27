import csv

# with open('mlb_players.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('new_players.csv', 'w') as new_csv:
#         csv_writer = csv.writer(new_csv, delimiter='-')
#
#         for line in csv_reader:
#             csv_writer.writerow(line)




    # next(csv_reader)
    # print(csv_reader)
    # for line in csv_reader:
    #     print(line)


with open('mlb_players.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_players.csv', 'w') as new_csv:

        field_name = ['Name',' "Age"', ' "Height(inches)"', ' "Team"', ' "Weight(lbs)"', ' "Position"']
        csv_writer = csv.DictWriter(new_csv, fieldnames=field_name,)
        csv_writer.writeheader()
        for row in csv_reader:
            csv_writer.writerow(row)



    # print(csv_reader)

    # for row in csv_reader:
    #     print(row['Name'])
