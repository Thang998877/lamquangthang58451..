"""
Author: Lâm Quang Thắng
Date: 16/09/2021
Program:
  Write a code segment that displays the values of the integers x, y, and z on a single
  line, such that each value is right-justified with a field width of 6.
Solution:

    ....
"""
x = int(input("nhap so dau tien: "))
y = int(input("nhap so dau tien: "))
z = int(input("nhap so dau tien: "))

print('%6d\n%6d\n%6d' %(x,y,z))