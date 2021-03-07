#!/usr/bin/python env

## http://open-notify.org

import requests
import json
from datetime import datetime

"""
    json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
    json.loads() — Takes a JSON string, and converts (loads) it to a Python object.
"""

response = requests.get("http://api.open-notify.org/astros.json")
print(f"Status Code: {response.status_code}")
print(f"{json.dumps(response.json(), sort_keys=True, indent=4)}")

# adding parameters 
parameters = {
    "lat": 40.71,
    "lon": -74
}

print()
print("### Passing of International Space Station ###")
res = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(f"{json.dumps(res.json(), sort_keys=True, indent=4)}")

# extracting pass times of iss 
passTimes = res.json()['response']
print(passTimes)

riseTimes = []
for pTime in passTimes:
    time = pTime['risetime']
    riseTimes.append(time)

print(riseTimes)

# converting rise times from timestamp to understable format 
times = []
for rTime in riseTimes:
    dateTime = datetime.fromtimestamp(rTime)
    print(dateTime)