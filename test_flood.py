"""Unit test for the flood module"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from random import choice

stations = build_station_list(use_cache=True)
update_water_levels(stations)

def test_stations_level_over_threshold():
    tol = 0.8    
    flooded_stations = stations_level_over_threshold(stations, tol)
    for station_tuple in flooded_stations:
        assert station_tuple[1] > tol

def test_stations_highest_rel_level():
    chosen_station = choice(stations)
    chosen_station.latest_level = 999
    highest_stations = stations_highest_rel_level(stations, 1)
    assert highest_stations[0][0].name == chosen_station.name
    assert highest_stations[0][1] == chosen_station.latest_level
    assert len(highest_stations) == 1
