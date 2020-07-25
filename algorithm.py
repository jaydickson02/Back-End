# Jay, this isn't javascript. Fight me! Actually don't im scared
import json
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='')
# Api Stuff Goes here


# Main code loop

data = {
    'start': 1000,
    'end': 1400,
    'location': 'North Melbourne'  # Coordinate system or use google converter
}


# Algorithm Pipeline
# Api key:
# Install this boi:  pip install -U googlemaps


data_json = json.dumps(data)

# send to pikey
print(data_json)
