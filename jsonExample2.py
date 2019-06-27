import json

with open('states.json', 'r') as f:
    data = json.load(f)

# print(data)
for state in data['states']:
    for s,v in state.items():
        print(s,v)
    # print(state)
    # print(state['name'], state['abbreviation'])







    # print(state['name'], state['abbreviation'])
