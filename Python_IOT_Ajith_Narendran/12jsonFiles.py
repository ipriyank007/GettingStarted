# JavaScript object Notation

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

for i in data['People']:
    print(i['Name'], i["Have_license"])
