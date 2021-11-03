"""
Author: Lâm Quang Thắng
Date: 24/10/2021
Program:
  Viết mã cho một ánh xạ tạo ra một danh sách các giá trị tuyệt đối của các số trong một danh sách có tên là các số.
Solution:

    ....
"""

a = [5, -6, 7, -8, -10]
print("The original list is : " + str(a))
b = list(map(abs, a))
print("Absolute value list : " + str(b))
