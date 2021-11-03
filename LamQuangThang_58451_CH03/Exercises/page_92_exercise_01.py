"""
Author: Lâm Quang Thắng
Date: 16/09/2021
Program:
  Translate the following for loops to equivalent while loops:
a. for count in range(100):
 print(count)
b. for count in range(1, 101):
 print(count)
c. for count in range(100, 0, –1):
 print(count)

Solution:
a. count = 0
while count <= 100:
 count += 1
 print(count)

b.count = 0
b = 1
while count <= 101:
 count += b
 b += 1
 print(count)

 c.count = 100
while count >= 1:
 print(count, end = " ")
 count -= 1

    ....
"""

