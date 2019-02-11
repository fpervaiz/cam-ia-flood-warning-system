"""This module provides functions for calculating polynomial best fits
for historical data"""

from matplotlib.dates import date2num

import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """Finds the best-fit polynomial of degree p and returns the polynomial and date-shift"""
    x = date2num(dates)
    y = levels
    d0 = x[0]
    p_coeff = np.polyfit(x - d0, y, p)
    poly = np.poly1d(p_coeff)

    return (poly, d0)

def level_is_rising(poly, d0, dates):
    """Returns true if the gradient of a given best-fit polynomial at a given date is rising"""
    x = date2num(dates[-1])
    grad_poly = np.polyder(poly)
    grad = grad_poly(x - d0)
    if grad > 0:
        return True
    else:
        return False