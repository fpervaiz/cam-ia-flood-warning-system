"""Unit test for the analysis submodule"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import level_is_rising, polyfit, get_threat_level
from random import choice

import datetime
import numpy as np

stations = build_station_list(use_cache=True)
update_water_levels(stations)

station = choice(stations)

def test_polyfit():
    dt = 10
    degree = 4
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    poly, d0 = polyfit(dates, levels, degree)
    assert poly
    assert d0

def test_level_is_rising():
    dates = np.array((1, 2, 3))
    poly = np.poly1d(np.array((1, 0, 0))
    d0 = 0
    assert level_is_rising(poly, d0, dates)

def test_get_threat_level():
    assert get_threat_level(True, 1.6) == "Severe"