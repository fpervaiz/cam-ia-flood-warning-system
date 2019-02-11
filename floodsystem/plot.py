"""This module provides functions for plotting and analysing
historical water level data for monitoring stations"""

import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
from matplotlib.dates import date2num

def plot_water_levels(station, dates, levels):
    """Creates a matplotlib plot of the water level data against time for a station
    with typical high and low levels."""
    plt.plot(dates, levels)
    if station.typical_range:
        low, high = station.typical_range
        plt.axhline(low, color='r', linestyle='--')
        plt.axhline(high, color='r', linestyle='--')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level data and the best-fit polynomial for given station."""
    poly, d0 = polyfit(dates, levels, p)
    plt.plot(dates, levels)
    if station.typical_range:
        low, high = station.typical_range
        plt.axhline(low, color='r', linestyle='--')
        plt.axhline(high, color='r', linestyle='--')
    x = date2num(dates)
    plt.plot(x, poly(x - d0), color='m')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    plt.tight_layout()
    plt.show()
    return poly, d0
