from floodsystem.flood  import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import level_is_rising, polyfit

import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    highest_stations = stations_highest_rel_level(stations, 5)

    for station_tuple in highest_stations:
        station = station_tuple[0]
        dt = 2
        degree = 4
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        poly, d0 = polyfit(dates, levels, degree)
        rel_level = station.relative_water_level()
        rising = level_is_rising(poly, d0, dates)

        # TODO: use gradient at latest level to determine if rising or falling
        # Severe: Above typical max and rising
        # High: >75% of typical max and rising or above typical max and falling
        # Moderate: >75% of typical max and falling or >50% of typical max and rising
        # Low: if none of above

        if rel_level >= 1 and rising or rel_level >= 1.5:
            threat = "Severe"
        elif rel_level >= 0.75 and rising or rel_level >=1 and not rising:
            threat = "High"
        elif rel_level >= 0.75 and not rising or rel_level >= 0.5 and rising:
            threat = "Moderate"
        else:
            threat = "Low"
        print(station.name, threat)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()