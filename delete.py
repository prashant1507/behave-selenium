import json
import behave2cucumber
with open('reports/json/a.json') as behave_json:
    cucumber_json = behave2cucumber.convert(json.load(behave_json))
    print(cucumber_json)