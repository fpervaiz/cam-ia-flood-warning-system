from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

location_coord = (52.2053, 0.1218)

def run():
    """Requirements for Task 1B"""

    stations = build_station_list()
    results = stations_by_distance(stations, location_coord)

    # Ten closest
    closest = list()
    for result in results[:10]:
        station, distance = result
        closest.append((station.name, station.town, distance))

    # Ten furthest
    furthest = list()
    for result in results[-10:]:
        station, distance = result
        furthest.append((station.name, station.town, distance))
    
    print("\nTen closest stations from {}:".format(location_coord))
    print(closest)
    print("\nTen furthest stations from {}:".format(location_coord))
    print(furthest)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()