#!/usr/bin/python env

# https://unsplash.com/developers
# https://unsplash.com/documentation/

"""
* params for /photo/random
1. collections 	Public collection ID(‘s) to filter selection. If multiple, comma-separated
2. topics 	    Public topic ID(‘s) to filter selection. If multiple, comma-separated
3. username 	    Limit selection to a single user.
4. query 	        Limit selection to photos matching a search term.
5. orientation 	Filter by photo orientation. (Valid values: landscape, portrait, squarish)
6. content_filter Limit results by content safety. Default: low. Valid values are low and high.
7. count 	        The number of photos to return. (Default: 1; max: 30)

* params for /photos/:id/download
1. id 	        The photo’s ID. Required.

* params for /search/photos
1. query 	        Search terms.
2. page 	        Page number to retrieve. (Optional; default: 1)
3. per_page 	    Number of items per page. (Optional; default: 10)
4. order_by 	    How to sort the photos. (Optional; default: relevant). Valid values are latest and relevant.
5. collections 	Collection ID(‘s) to narrow search. Optional. If multiple, comma-separated.
6. content_filter Limit results by content safety. (Optional; default: low). Valid values are low and high.
7. color 	Filter  results by color. Optional. Valid values are: black_and_white, black, white, yellow, orange, red, purple, magenta, green, teal, and blue.
8. orientation 	Filter by photo orientation. Optional. (Valid values: landscape, portrait, squarish)

* params for /search/collection
1. query 	        Search terms.
2. page 	        Page number to retrieve. (Optional; default: 1)
3. per_page 	    Number of items per page. (Optional; default: 10)
"""
import json
import requests

with open('accesskey', 'r') as f:
    accesskey = f.readline()

header = {
    "Authorization": accesskey,
    "content-type": "application/json" 
}

endpoint = "https://api.unsplash.com/"
photosRandom = f'{endpoint}/photos/random'

searchPhotos = f'{endpoint}/search/photos'
searchCollection = f'{endpoint}/search/collection'

searchPhotosParam = {
    "query": "New York"
}

searchCollecParams = { 
    "query": "Landscapes"
}

# get random photos
res = requests.get(photosRandom, headers=header)
print(json.dumps(res.json(), sort_keys=True, indent=4))

# search photos collection
res = requests.get(searchCollection, headers=header, params=searchCollecParams)
print(json.dumps(res.json(), sort_keys=True, indent=4))

# search photos using a specific keyword
res = requests.get(searchPhotos, headers=header, params=searchPhotosParam)
print(json.dumps(res.json(), sort_keys=True, indent=4))


# tracking an image download /photos/:id/download
download = f"{endpoint}/photos/{res.json()['id']}/download"
res = requests.get(download, headers=header)

print(json.dumps(res.json(), sort_keys=True, indent=4))

