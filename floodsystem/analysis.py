from matplotlib.dates import date2num

import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    x = date2num(dates)
    y = levels
    d0 = x[0]
    p_coeff = np.polyfit(x - d0, y, p)
    poly = np.poly1d(p_coeff)

    return (poly, d0)