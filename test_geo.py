"""Unit test for the geo module"""

from floodsystem.geo import haversine, stations_by_distance, stations_within_radius

def test_haversine():
    """Test haversine distance calculation."""

    c1 = (52.2053, 0.1218) # Cambridge City Centre
    c2 = (52.1985, 0.1208) # CUED
    known_distance = 0.764

    assert haversine(c1, c2) == known_distance



