#!/usr/bin/python env

# https://api.le-systeme-solaire.net/en/

import requests
import json
import argparse
import sys

parser = argparse.ArgumentParser(description="Properties of Solar System Planets")
parser.add_argument("-f", "--format", help="shows the information in a json format", action="store_true")
parser.add_argument("-p", "--properties", help="prints all supported properties by the api", action="store_true")
args = vars(parser.parse_args())

# formatting in a json format
formatJson = args['format']
# properties
prop = args['properties']

if prop:
    print("All supported prpertie")
    with open("properties", "r") as f:
        properties = f.readlines()
    for i in properties:
        print(i.rstrip("\n"))
    # exit the program
    sys.exit(0)

# read again for information grabbing see the printing part
with open("properties", "r") as f:
    properties = f.readlines()

def getResponse(obj):
    uri = "https://api.le-systeme-solaire.net/rest/bodies/" + obj
    response = requests.get(uri)
    return response

print("Guide To Solar System")
print("---------------------")
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

# printing planets name and their number
for i in range(0, len(planets)):
    print(f"{i + 1}. {planets[i]}")

print()
info = int(input("Enter Number of any above Planet: "))
information = getResponse(planets[info - 1])

if formatJson:
    print("Formatting the response from the api in JSON form")
    print("-------------------------------------------------")
    print(json.dumps(information.json(), indent=4, sort_keys=True))
else:

    print(f"Display All Properties of {planets[info]} ")
    print("--------------------------------")

    for i in range(0, len(properties)):
        pr = (properties[i].rstrip("\n"))

        info = information.json()[pr]

        if pr == "moons":
            moon = information.json()["moons"]
            if moon:
                for sat in moon:
                    print("*** Moon(s) ***")
                    print(f"moon: {sat['moon']}")
        elif pr == "mass":
            print("*** Mass ***")
            print(f"massValue: {info['massValue']}")
            print(f"massExponent: { info['massExponent']}")
        elif pr == "vol":
            print("*** Volume(s) ***")
            print(f"volValue: {info['volValue']}")
            print(f"volExponent: { info['volExponent']}")
        else:
            print(f"{pr}: {info}")
