# ---------------------
# POI Distance Function
# ---------------------

import json
from osgeo import ogr
import numpy as np


def title():
    return "POI Distance Calculator"  # title of the function


def abstract():
    return "A function to calculate the distance between the POI and a specified building feature"  # short description of the function


def inputs():
    return [
        ['building', 'Input Feature 1', 'Building GeoJSON file', 'application/json', True],
        ['poi', 'Input Feature 2', 'POIs GeoJSON', 'application/json', True]
           ]

def outputs():
    return [
        ['result', 'POI distance', 'The distance between POI and building', 'application/json']]


def execute(parameters):
    building = parameters.get('building')
    poi = parameters.get('poi')



    if (building is not None) and (poi is not None):
        building = building['value']
        poi = poi['value']


    b_ = ogr.CreateGeometryFromJson(building)
    p_ = ogr.CreateGeometryFromJson(poi)


    result = p_.Distance(b_)

    print("Content-type: application/json")
    print()
    print('The distance between the restaurant and the ITC Hotel is %.2f metres'%result)
