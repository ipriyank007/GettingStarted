import json

people_info = '''
{
    "data": [
    {
        "name": "Sam",
        "age": 23,
        "have_license": true,
        "pan_number": "34DDSAW112D"
    },
    {
        "name": "Robert",
        "age": 42,
        "have_license": false,
        "pan_number": null
    }
]
}
'''
# json to python conversions:
# json string ("") to python string ('')
# json real number to python float
# json integer numbers to python int
# json boolean (lower case true/false) to python uppercase True and False
# json null to python's None
# json array to python's list
# json object to python's dictionary

data = json.loads(people_info)
print(data)

