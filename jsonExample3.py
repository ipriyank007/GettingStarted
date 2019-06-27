import json
from urllib.request import urlopen

with urlopen("https://gist.githubusercontent.com/VerizonMediaOwner/"
             "a4f27c0c04358b343f4a2308ea903cb8/raw/917ca865813d5047"
             "96ccae1d1643584d526473de/weather_ydn_js.json") as response:
    source = response.read()

data = json.loads(source)

for temp in data["forecasts"]:
    if temp['day'] == 'Thu':
        print(temp['low'], temp['high'])

# print(json.dumps(data, indent=3))
