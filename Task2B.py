from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""
    
    stations = build_station_list()
    update_water_levels(stations)
    tol=0.8
    
    flooded_stations=stations_level_over_threshold(stations,tol)
    
    for station in flooded_stations:
        print(station[0], station[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System *** \n")
    run()

