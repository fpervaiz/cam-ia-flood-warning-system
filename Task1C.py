from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

location_coord = (52.2053, 0.1218)
radius = 10

def run():
    """Requirements for Task 1C"""

    stations = build_station_list()
    valid_stations = stations_within_radius(stations, location_coord, radius)

    station_names = list()
    for station in valid_stations:
        station_names.append(station.name)

    print("\nThe following stations are within {}km of {}:".format(radius, location_coord))
    print(station_names)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()