from floodsystem.flood  import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels

import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    highest_stations = stations_highest_rel_level(stations, 5)

    for station_tuple in highest_stations:
        station = station_tuple[0]
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()