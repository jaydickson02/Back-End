""" Module Docstring following Google Style Guide

This is a cloud function that does the googley moogley

Todo:
    * Write the function
"""
#from datetime import datetime
import json

import googlemaps

# get our googley boi
k = open('apiKey.txt', 'r')
gmaps = googlemaps.Client(key=k.read())

data = {
    'start': 1000,
    'end': 1400,
    'location': 'North Melbourne'  # Coordinate system or use google converter
}

# Algorithm Pipeline
# get list of all places in North Melbourne
# Filter out places that are not open during start and end time
# get popularity data, sort remaining places by popularity during open hours

data_json = json.dumps(data)

print(data_json)
