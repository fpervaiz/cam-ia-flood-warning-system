from floodsystem.flood  import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import level_is_rising, polyfit, get_threat_level
from floodsystem.utils import send_email
from floodsystem.geo import stations_within_radius, stations_by_distance

import datetime

# Name, email, location, warning radius (km)
recipients = [('Finn Chapman', 'fac33@cam.ac.uk', (52.21, 0.103), 20),
('Faizaan Pervaiz', 'fp361@cam.ac.uk', (51.86, -2.23), 20)]

def run():
    stations = build_station_list()
    update_water_levels(stations)

    for recipient in recipients:
        name = recipient[0]
        email = recipient[1]
        centre = recipient[2]
        radius = recipient[3]

        stations_to_check = stations_within_radius(stations, centre, radius)
        dt = 2
        degree = 4
        counter = 1
        max = len(stations_to_check)
        failed_stations = list()
        for station in stations_to_check:
            print("Processing station {} of {} for {}".format(counter, max, name), end='\r')
            counter += 1
            if station.threat == "Unavailable":
                dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
                try:
                    poly, d0 = polyfit(dates, levels, degree)
                except IndexError:
                    failed_stations.append(station)
                    continue
                rel_level = station.relative_water_level()
                rising = level_is_rising(poly, d0, dates)
                station.set_threat(get_threat_level(rising, rel_level))

        send_stations = stations_by_distance(stations_to_check, centre)
        send_failed_stations = stations_by_distance(failed_stations, centre)
        print("\n"+str(send_email(name, email, radius, send_stations, send_failed_stations)))


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()