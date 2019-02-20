# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""

import requests

def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

def send_email(name, email, radius, stations, failed_stations):
  """Constructs an email containing flood alerts and sends to the specified recipient"""
  num_severe, num_moderate, num_high, num_low = 0, 0, 0, 0
  text = "Here are the threat levels for flood stations within " + str(radius) + "km of your location, in order of increasing distance. Stations with severe threat are shown in bold.<br>"
  for station_tuple in stations:
    station = station_tuple[0]
    distance = station_tuple[1]

    if station.threat == "Severe":
      num_severe += 1
    elif station.threat == "High":
      num_high += 1
    elif station.threat == "Moderate":
      num_moderate += 1
    else:
      num_low += 1

    if station.threat == "Severe":
      text += "<br><b>" + station.name + " (" + str(distance) + "km) : " + station.threat + "</b>"
    else:
      text += "<br>" + station.name + " (" + str(distance) + "km) : " + station.threat
  
  text += "<br><br>Summary:<br><b>Severe: {}</b><br>High: {}<br>Moderate: {}<br>Low: {}<br>".format(num_severe, num_high, num_moderate, num_low)
  text += "<br><br>Threat level data was not available for the following stations:<br><br>"
  for station_tuple in failed_stations:
    station = station_tuple[0]
    distance = station_tuple[1]
    text += station.name + " (" + str(distance) + "km)<br>"
  
  return requests.post("https://api.mailgun.net/v3/sandboxecefc31ea7a94362a510cb1c01eb18fb.mailgun.org/messages",
        auth=("api", "627188ef52e1322360915ee73184cc42-1b65790d-e7a6f0ed"),
        data={"from": "Flood Alerts <postmaster@sandboxecefc31ea7a94362a510cb1c01eb18fb.mailgun.org>",
              "to": email,
              "subject": "Flood Alerts - CUED IA Computing",
              "html": text})