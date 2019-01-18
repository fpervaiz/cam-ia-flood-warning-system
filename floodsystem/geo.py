# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

import math
from .utils import sorted_by_key  # noqa

def haversine(coord1, coord2):
    """Returns the distance in km between two coordinate points on the globe."""

    lon1, lat1 = coord1
    lon2, lat2 = coord2

    R = 6371000
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2-lat1)
    delta_lambda = math.radians(lon2-lon1)

    a = math.sin(delta_phi/2.0)**2 + math.cos(phi_1)*math.cos(phi_2)*math.sin(delta_lambda/2.0)**2
    
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))

    distance = round(R*c/1000, 3)

    return distance

def stations_by_distance(stations, p):
    """Returns a list of (station, distance) tuples sorted by distance given a list of stations and an origin coordinate."""

    station_distance_list = list()
    for station in stations:
        distance = haversine(station.coord, p)
        station_distance_list.append((station, distance))
    return sorted_by_key(station_distance_list, 1)

def stations_within_radius(stations, centre, r):
    """Returns a list of stations within distance in km 'r' from coordinate 'centre' given list of input stations."""

    valid_stations = list()
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            valid_stations.append(station)

    return valid_stations