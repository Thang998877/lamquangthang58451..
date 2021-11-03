"""
Author: Lâm Quang Thắng
Date: 06/09/2021
Problem:
   An object’s momentum is its mass multiplied by its velocity.
   Write a program that accepts an object’s mass (in kilograms) and velocity (in meters per second) as inputs and then outputs its momentum.
Solution:
    ....
"""

# Request the input
mass = float(input("Enter the object's mass = "))
velocity = float(input("Enter the object's  velocity = "))

#Compute the results
momentum = mass * velocity

# Display the results
print("Momentum = ",momentum )