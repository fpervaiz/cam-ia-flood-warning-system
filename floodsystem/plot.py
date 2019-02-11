"""This module provides functions for plotting and analysing
historical water level data for monitoring stations """

import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    """Creates a matplotlib plot of the water level data against time for a station
    with typical high and low levels"""
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    plt.tight_layout()
    plt.show()