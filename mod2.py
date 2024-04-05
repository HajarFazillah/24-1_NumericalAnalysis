import numpy as np

def calc_area_ractangle(width, height=None):
    if height is None:
        height=width
    return width*height

def calc_area_circle(radius):
    return np.pi*(radius**2)