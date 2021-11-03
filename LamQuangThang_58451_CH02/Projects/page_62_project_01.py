"""
Author: Lâm Quang Thắng
Date: 06/09/2021
Problem:
   The tax calculator program of the case study outputs a floating-point number that might show more than two
   digits of precision. Use the round function to modify the program to display at most two digits of precision
   in the output number.
Solution:
    ....
"""
# Initialize the cóntants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request the inputs
grossincome = float(input("Enter the gross income :"))
numberofdependents = int(input("Enter the number of dependents :"))

# Compute the income tax
taxableincome = grossincome - STANDARD_DEDUCTION - \
                DEPENDENT_DEDUCTION * numberofdependents
incomeTax = taxableincome * TAX_RATE

# Display the income tax
print("the income tax is $"+ str(round(incomeTax,2)))
