#!/usr/bin/python env


##### see https://developer.spotify.com/documentation/web-api/

import requests
import base64
from urllib.parse import urlencode
import json

# create a file called clientinfo in the same folder as this class
# enter the client id on the first line without qouation marks
# enter the client secret on the second line without quoation marks

# for authorization flows and access token see
# https://developer.spotify.com/documentation/general/guides/authorization-guide/

with open("clientInfo", "r") as f:
    data = f.readlines()

# removing extra spaces or newline
for i in range(0, len(data)):
    data[i] = data[i].strip("\n")

# first line is client id 
clientId = data[0]
# second line is client secret
clientSecret = data[1]

# endpoints
tokenUrl = "https://accounts.spotify.com/api/token"
searchUrl = "https://api.spotify.com/v1/search"

# get token from the api
class SpotifyApi(object):

    def __init__(self, clientId, clientSecret, tokenUrl, searchUrl):
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.tokenUrl = tokenUrl
        self.searchUrl = searchUrl

    # returns a based encoded string 
    def getBased64EncodedString(self):
        clientId = self.clientId
        clientSecret = self.clientSecret

        auth = f"{clientId}:{clientSecret}"
        auth64 = base64.b64encode(auth.encode())
        return auth64.decode()

    # generate any dictionary resource 
    def generateResource(self, header):
        key = [x[0] for x in header]

        value = [x[1] for x in header]
        resource = {}
        for i in range(0, len(key)):
            resource[key[i]] = value[i]
        return resource

    def handleAuth(self, data, headers):
        r = requests.post(self.tokenUrl, data=data, headers=headers)
        response = r.json()

        if r.status_code in range(200, 299):
            accessToken = response['access_token']
            expires = response['expires_in']
            return accessToken

    def searchSong(self, headers, query, searchType="track", market="US", limit=1):
        print("Searching..")
        # if the passed query is a dictionary
        if isinstance(query, dict):
            i = [f"{k}:{v}" for k, v in query.items()]
            print(i)
            # replace a string query into a dictionary one
            query = " ".join(i)

        # construct a query and encode it using urlencode
        queryParam = urlencode({"q": query, "type": searchType.lower(), "market": market , "limit":limit})
        # constructing the look up address/ endpoint address 
        lookUp = f"{self.searchUrl}?{queryParam}"
    
        r = requests.get(lookUp, headers=headers)
    
        # responses status is 200-299 (ok)
        if r.status_code in range(200, 299):
            print(json.dumps(r.json(), sort_keys=True, indent=4))
            return r.json()



if __name__ == "__main__":
    spotify = SpotifyApi(clientId, clientSecret, tokenUrl, searchUrl)

    # access token for the spotify api
    # generating data for access token
    data = spotify.generateResource([('grant_type', 'client_credentials')])
    decodedClientId = spotify.getBased64EncodedString()
    # generating header for access token 
    headers = spotify.generateResource([('Authorization', f'Basic {decodedClientId}')])
    # performing the authorization and returing the access token 
    accessToken = spotify.handleAuth(data, headers)

    # searches a song using spotify api
    headers = spotify.generateResource([('Authorization', f'Bearer {accessToken}')])
    # create a dictionary resource to search
    data = spotify.generateResource([("track", "In The Night"), ("artist", "The Weeknd")])
    # searching a song using the dictionary search 
    spotify.searchSong(headers, data)
