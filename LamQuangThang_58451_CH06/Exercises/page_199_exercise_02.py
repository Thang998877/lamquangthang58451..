"""
Author: Lâm Quang Thắng
Date: 24/10/2021
Program:
  Viết mã cho một bộ lọc tạo ra một danh sách các số dương trong một danh sách
số được đặt tên. Bạn nên sử dụng lambda để tạo hàm phụ
Solution:

    ....
"""
a = [34, 1, 0, -23, 12, -88, 69, 107,90]
print("Original numbers in the list: ",a)
print("Positive numbers in the said list: ")
for pos_nums in a:
   if pos_nums > 0:
      print(pos_nums, end = " ")
