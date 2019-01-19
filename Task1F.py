from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""

    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    station_names = list()
    for station in inconsistent_stations:
        station_names.append(station.name)

    print("\nThe following stations have inconsistent low/high range data:\n")
    print(sorted(station_names))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()