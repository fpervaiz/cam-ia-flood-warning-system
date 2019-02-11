"""This module contains a collection of functions relating to a flood event."""


def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples, where each contains the name of a station at which the relative
    water level is above tol and the relative water level at that station"""

    flooded_stations = []

    for station in stations:
        relative_level = station.relative_water_level()
        try:
            if relative_level > tol:
                flooded_stations.append((station.name, relative_level))
        except:
            pass

    flooded_stations.sort(key=lambda x: x[1], reverse=True)
    return flooded_stations

def stations_highest_rel_level(stations, N):
    """Returns a descending list of the N stations at which the water level,
    relative to the typical range, is highest"""

    stations_rel_level = []

    for station in stations:
        relative_level = station.relative_water_level()

        # only append if relative level is present
        if relative_level != None:
            stations_rel_level.append((station, relative_level))

        stations_rel_level.sort(key=lambda x: x[1], reverse=True)
        flooded_stations = stations_rel_level[:N]

    return flooded_stations