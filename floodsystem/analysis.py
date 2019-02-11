import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    poly, d0 = polyfit(dates, levels, 3)
    return (poly, d0)