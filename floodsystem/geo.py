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

def rivers_with_stations(stations):
    """Returns a set with the names of any rivers with a monitoring station"""
    counter = 0
    valid_rivers = set()
    while counter < len(stations):
        valid_rivers.add(stations[counter].river)
        counter += 1
        if counter > 200000:
            break
        else:
            pass
        
    return valid_rivers

def stations_by_river(stations):
    """Returns a dict that maps river names (as keys) to a list of station objects on the river"""

    river_dict = dict()
    for station in stations:
        if station.river in river_dict:
            river_dict[station.river].append(station.name)
        else:
            river_dict[station.river] = [station.name]

    return river_dict
       

def rivers_by_station_number(stations, N):
    "Returns a list of tuples of the N greatest rivers by number of stations"
    stat_dict = stations_by_river(stations)
    station_numbers = {w:len(d) for w, d in stat_dict.items()}
    station_numbers_by_value = sorted(station_numbers.items(), key=lambda wd: wd[1], reverse=True)
    for n in range(len(station_numbers_by_value)):
        if station_numbers_by_value[N+n][1] > station_numbers_by_value[N+n+1][1]:
            y = station_numbers_by_value[:N+n]
            break
        else:
            pass
    return y

    