"""
Author: Lâm Quang Thắng
Date: 06/09/2021
Problem:
   The kinetic energy of a moving object is given by the formula KE = 1/2*m*v**2
   where m is the object’s mass and v is its velocity.
   Modify the program you created in Project 5 so that it prints the object’s kinetic energy as well as its momentum.

Solution:
   Human beings, desktop computers, cellphones
    ....
"""
# Request the input
mass = float(input("Enter the mass = "))
velocity = float(input("Enter the velocity = "))

# Compute the results
momentum = mass * velocity
kineticEnergy = (mass * velocity ** 2) /2

# Display the results
print("Momentum = ",momentum )
print("Kinetic Energy = ",kineticEnergy)