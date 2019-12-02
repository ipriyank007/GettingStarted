import json

with open('states.json', 'r') as f:
    states = json.load(f)
    for state in states['states']:
        print(state["area_codes"][0])    
    states_json = json.dumps(states, indent=2)
    with open('states_new.json', 'w') as wf:
        wf.write(states_json)
    
