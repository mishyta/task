import json
from pathlib import Path
import pickle
import pandas as pd

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

########
# JSON #
########


str = json.dumps(SELENOID,indent= 4) # Encoding basic Python object to json
print(str)
conf = json.loads(str) # Decoding JSON to basic Python object
print(conf)

# json =   {"SELENOID_OPTIONS": {"enableVNC": true, "enableVideo": null}, "CAPABILITIES_FF": {"browserName": "firefox", "browserVersion": 92.0, "selenoid:options": "SELENOID_OPTIONS"}}
# Python = {'SELENOID_OPTIONS': {'enableVNC': True, 'enableVideo': None}, 'CAPABILITIES_FF': {'browserName': 'firefox', 'browserVersion': 92.0, 'selenoid:options': 'SELENOID_OPTIONS'}}



with open('selenoid.json', 'w') as write_file: # Write basic Python object to json file 
    json.dump(SELENOID, write_file,indent=4)
ls()
fpath = Path.cwd() / 'selenoid.json'
print(fpath.read_text())

with open('selenoid.json', 'r') as f:# Read basic Python object from json file 
    conf = json.load(f)


##########
# PICKLE #
##########


str = pickle.dumps(SELENOID) # Encoding basic Python object to bytes
print(str)
conf = pickle.loads(str) # Decoding bytes to basic Python object
print(conf)

# bytes  = b'\x80\x04\x95\x95\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x10SELENOID_OPTIONS\x94}\x94(\x8c\tenableVNC\x94\x88\x8c\x0benableVideo\x94Nu\x8c\x0fCAPABILITIES_FF\x94}\x94(\x8c\x0bbrowserName\x94\x8c\x07firefox\x94\x8c\x0ebrowserVersion\x94G@W\x00\x00\x00\x00\x00\x00\x8c\x10selenoid:options\x94h\x01uu.'
# python = {'SELENOID_OPTIONS': {'enableVNC': True, 'enableVideo': None}, 'CAPABILITIES_FF': {'browserName': 'firefox', 'browserVersion': 92.0, 'selenoid:options': 'SELENOID_OPTIONS'}}

with open('selenoid.pickle', 'wb') as write_file: # Write basic Python object to json file 
    pickle.dump(SELENOID, write_file)


print(pd.read_pickle('selenoid.pickle'))

with open('selenoid.pickle', 'rb') as f:# Read basic Python object from json file 
    conf = pickle.load(f)