# JavaScript Object Notation
# To parse and generate Json files.
import json

people_info = '''
{
    "People": [
        {
            "Name": "Priyank",
            "Age": 28,
            "DOB": "15-08-1994",
            "Have_license":false
        },
        {
            "Name": "Vendy",
            "Age": 25,
            "DOB": "25-04-1993",
            "Have_license":true
        }
    ]
}
'''

data = json.loads(people_info)
# print(data)

for person in data['People']:
    # print(person['Name'])
    del person['Age']

new_string = json.dumps(data, indent=4, sort_keys=True)
print(new_string)
