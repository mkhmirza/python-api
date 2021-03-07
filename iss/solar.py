#!/usr/bin/python env

# https://api.le-systeme-solaire.net/en/

import requests
import json


def getResponse(obj):
    uri = "https://api.le-systeme-solaire.net/rest/bodies/" + obj
    response = requests.get(uri)
    return response

print("Guide To Solar System")
print("######################")
print("Sun")
print("Mercury")
print("Venus")
print("Earth")
print("Mars")
print("Jupiter")
print("Saturn")
print("Uranus")
print("Neptune")
print("Pluto (Dwarf Planet)")


print()
info = input("Enter Name of any above Planet or Star: ")
info = info.lower()

information = getResponse(info)

print()
print(f"Some facts for {info} ")
print("######################")

# print with formatting 
name = information.json()["englishName"]
moon = information.json()["moons"]

if moon:
    moons = []

    for sat in moon:
        m = sat['moon']
        moons.append(m)

mass = information.json()["mass"]["massValue"]

gravity = information.json()["gravity"]
density = information.json()["density"]

print(f"Name: {name}")
print(f"Mass: {mass}")
print(f"Gravity: {gravity}")
print(f"Density: {density}")
if moon: 
    for m in range(0,len(moons)):
        print(f"Moon#{m+1} = {moons[m]}")
else:
    print("Moon: None")

