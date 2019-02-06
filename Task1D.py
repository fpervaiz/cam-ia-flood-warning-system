from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""
    
    stations = build_station_list(use_cache=True)
    rivers_list = list(rivers_with_stations(stations))

    # Demonstrating rivers_with_station function
    print('Number of rivers with a monitoring station = ' + str(len(rivers_list)))
    sorted_rivers = sorted(rivers_list)
    
    print('First ten rivers with a station by alphabetical order: ' + str(sorted_rivers[:10]))


    

    # Demonstrating stations_by_river function    
    rivers_dict = stations_by_river(stations)

    aire_stations = sorted(rivers_dict["River Aire"])
    cam_stations = sorted(rivers_dict["River Cam"])
    thames_stations = sorted(rivers_dict["River Thames"])

    print('\nStations on the River Aire: ' + str(aire_stations))
    print('\nStations on the River Cam: ' + str(cam_stations))
    print('\nStations on the Thames: ' + str(thames_stations))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

