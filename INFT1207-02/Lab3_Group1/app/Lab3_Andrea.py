# Name: Andrea Magalhaes
# Date: October 20, 2024
# File Name: Lab 3
# Description: Calculates the area of four different types of shapes

from math import pi


def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")


def trapezium_area(a, b, h):
    # For each input, check if it is a float or an integer and if it is less than zero
    if not isinstance(a, (int, float)) or a < 0:
        return "Invalid! Must be a non-negative number!"
    elif not isinstance(b, (int, float)) or b < 0:
        return "Invalid! Must be a non-negative number!"
    elif not isinstance(h, (int, float)) or h < 0:
        return "Invalid! Must be a non-negative number!"
    # if input is valid, calculate the area of the shape
    else:
        return 0.5 * (a + b) * h


def ellipse_area(a, b):
    # For each input, check if it is a float or an integer and if it is less than zero
    if not isinstance(a, (int, float)) or a < 0:
        return "Invalid! Must be a non-negative number!"
    elif not isinstance(b, (int, float)) or b < 0:
        return "Invalid! Must be a non-negative number!"
    # if input is valid, calculate the area of the shape
    else:
        return pi * a * b



def rhombus_area(d1, d2):
    # For each input, check if it is a float or an integer and if it is less than zero
    if not isinstance(d1, (int, float)) or d1 < 0:
        return "Invalid! Must be a non-negative number!"
    elif not isinstance(d2, (int, float)) or d2 < 0:
        return "Invalid! Must be a non-negative number!"
    # if input is valid, calculate the area of the shape
    else:
        return 0.5 * d1 * d2
