"""
Author: Lâm Quang Thắng
Date: 06/09/2021
Problem:
   Write a program that takes the radius of a sphere (a floating-point number) as input and then outputs
   the sphere’s diameter, circumference, surface area, and volume.
Solution:
    ....
"""
import math

# Compute the input
r = float(input("Enter the radius = "))

# Compute the results
d = r * 2
p = d * math.pi
a = 4 * (r ** 2) * math.pi
v = 4/3 * (r ** 3) * math.pi

# Display the resulets
print("Diameter =", d, "m")
print("Circumference =", p, "m")
print("Surface area =", a, "m**2")
print("Volume =", v, "m**3")