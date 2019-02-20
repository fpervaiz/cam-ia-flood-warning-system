"""Unit test for the analysis submodule"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import level_is_rising, polyfit, get_threat_level
from random import choice
from datetime import datetime, timedelta
from matplotlib.dates import date2num

import numpy as np

stations = build_station_list(use_cache=True)
update_water_levels(stations)

station = choice(stations)

def test_polyfit():
    dt = 10
    degree = 4
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
    poly, d0 = polyfit(dates, levels, degree)
    assert poly
    assert d0

def test_level_is_rising():
    dates = np.array((date2num(datetime(2019, 1, 1)), date2num(datetime(2019, 1, 2)), date2num(datetime(2019,1, 3))))
    levels = [1, 4, 9]
    degree = 4
    poly, d0 = polyfit(dates, levels, degree)
    assert level_is_rising(poly, d0, dates)

def test_get_threat_level():
    assert get_threat_level(True, 1.6) == "Severe"