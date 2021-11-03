"""
Author: Lâm Quang Thắng
Date: 06/09/2021
Problem:
   Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums.
   The store rents new videos for $3.00 a night, and oldies for $2.00 a night.
   Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals.
   The program should prompt the user for the number of each type of video and output the total cost.
Solution:
    ....
"""

# Initialize constans
NEW_RENTAL = 3.00
OLDIE_RENTAL = 2.00

# Request the inputs
newOnes = int(input("enter the number of new video: "))
oldOnes = int(input("enter the number of oldies: " ))

# Compute the results
totalCost =NEW_RENTAL * newOnes +OLDIE_RENTAL * oldOnes

# Dispplay the results
print("the total cost is $" + str(round(totalCost, 2)))