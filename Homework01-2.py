# Bradley Cox - Homework 01, Problem 2
# 01/31/2023

import math

# a function to perform various calculations
def radiusMath(radius):
    diameter = 2 * radius
    circumference = diameter * math.pi
    surfaceArea = 4 * math.pi * (radius**2)
    volume = (4/3) * math.pi * (radius**3)

    # print the calculations for the user to view
    print("Diameter      : " + str(diameter))
    print("Circumference : " + str(circumference))
    print("Surface Area  : " + str(surfaceArea))
    print("Volume        : " + str(volume))

# request the value of radius as input
# if the user inputs a non-numerical value, an error is thrown
try:
    radius = float(input("Please enter the radius of the sphere: "))
    radiusMath(radius)
except Exception:
    print("Error, the radius must be a number.")