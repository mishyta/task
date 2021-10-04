import json
from pathlib import Path

SELENOID ={
'SELENOID_OPTIONS': {
    "enableVNC": True,
    "enableVideo": None
},

'CAPABILITIES_FF': {
    "browserName": "firefox",
    "browserVersion": 92.0,
    "selenoid:options": 'SELENOID_OPTIONS'
},
}

str = json.dumps(SELENOID,indent= 4) # Encoding basic Python object to json
print(str)
conf = json.loads(str) # Decoding JSON to basic Python object
print(conf)

# {"SELENOID_OPTIONS": {"enableVNC": true, "enableVideo": null}, "CAPABILITIES_FF": {"browserName": "firefox", "browserVersion": 92.0, "selenoid:options": "SELENOID_OPTIONS"}}
# {'SELENOID_OPTIONS': {'enableVNC': True, 'enableVideo': None}, 'CAPABILITIES_FF': {'browserName': 'firefox', 'browserVersion': 92.0, 'selenoid:options': 'SELENOID_OPTIONS'}}



with open('selenoid.json', 'w') as write_file: # Write basic Python object to json file 
    json.dump(SELENOID, write_file,indent=4)

fpath = Path.cwd() / 'selenoid.json'
print(fpath.read_text())

with open('selenoid.json', 'r') as f:# Read basic Python object from json file 
    conf = json.load(f)


