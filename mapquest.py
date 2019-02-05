# Richmond Horikawa
# ID: 18715219

import urllib.parse
import urllib.request
import json

BASE_MAPQUEST_SEARCH_URL = 'http://open.mapquestapi.com/directions/v2/route'
BASE_MAPQUEST_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile'
MAPQUEST_API_KEY = 'E4wxVn3yMCnBzWeSrQcNd7NhwXu0IPAn'

def build_route_url(location_1: str, location_2: str) -> str:
    'Build the URL that gives information about the route'
    query_parameters = [
    ('key', MAPQUEST_API_KEY), ('from', location_1),
    ('to', location_2)
    ]

    return BASE_MAPQUEST_SEARCH_URL + '?' + urllib.parse.urlencode(query_parameters)

def build_elevation_url(latlongs: list) -> str:
    'Build the URL that give information about the elevation'
    latlong_collection = ''
    for coordinate in latlongs:
        latlong_collection = latlong_collection + str(coordinate) + ','
    latlong_collection = latlong_collection[:-1]
    query_parameters = [
    ('key', MAPQUEST_API_KEY), ('latLngCollection', latlong_collection),
    ('unit', 'f')
    ]

    return BASE_MAPQUEST_ELEVATION_URL + '?' + urllib.parse.urlencode(query_parameters)    

def check_result(url: str) -> dict:
    'Read the information presented in the URL and returns it as a dictionary'

    response = None

    try:
        response = urllib.request.urlopen(url)
        return json.load(response)

    finally:
        if response != None:
            response.close()

def return_directions(data: dict) -> list:
    'Read and return the directions given'
    directions = []
    for item in data['route']['legs']:
        for step in item['maneuvers']:
            directions.append(step['narrative'])
    return directions

def return_distance(data: dict) -> float:
    'Read and return the distance of the route to be taken'
    return data['route']['distance']

def return_time(data: dict) -> float:
    'Read and return the time of the trip to be taken'
    return data['route']['time']/60

def convert_lats(lat: float) -> str:
    'Convert the float value of lat and convert it to a string indicating S or N'
    lat = round(lat,2)
    if lat < 0:
        lat = lat * -1
        str_lat = ('%.2f' % lat)
        return str_lat + 'S'
    else:
        str_lat = ('%.2f' % lat)
        return str_lat + 'N'

def convert_longs(long: float) -> str:
    'Convert the float value of long and convert it to a string indicating W or E'
    long = round(long,2)
    if long < 0:
        long = long * -1
        str_long = ('%.2f' % long)
        return str_long + 'W'
    else:
        str_long = ('%.2f' % long)
        return str_long + 'E'

def return_first_latlongs(data: dict) -> list:
    'Read and return the coordinates of the first location'
    latlongs = []
    latlongs.append(data['route']['locations'][0]['displayLatLng']['lat'])
    latlongs.append(data['route']['locations'][0]['displayLatLng']['lng'])
    return latlongs

def return_last_latlongs(data: dict) -> list:
    'Read and return the coordinates of the second location'
    latlongs = []
    latlongs.append(data['route']['locations'][1]['displayLatLng']['lat'])
    latlongs.append(data['route']['locations'][1]['displayLatLng']['lng'])
    return latlongs
    
def return_latlongs(data: dict) -> list:
    'Read and return the coordinates of the first and second locations'
    latlongs = []
    latlongs.append(convert_lats(data['route']['locations'][0]['displayLatLng']['lat']))
    latlongs.append(convert_longs(data['route']['locations'][0]['displayLatLng']['lng']))
    latlongs.append(convert_lats(data['route']['locations'][1]['displayLatLng']['lat']))
    latlongs.append(convert_longs(data['route']['locations'][1]['displayLatLng']['lng']))
    return latlongs

def return_elevations(data: dict) -> int:
    'Read and return the elevation of the location'
    elevations = round(data['elevationProfile'][0]['height'])
    return elevations
    
