"""
Author: Lâm Quang Thắng
Date: 25/09/2021
Program:
 Viết một đoạn mã để mở một tệp có tên myfile.txt để nhập và in
số dòng trong tệp.
Solution:

    ....
"""
fname = "C:\Users\Techcare\Desktop\l.q.thang_python\Writing_code_Python\Learning_Python_in_book\LamQuangThang_58451_CH04v\Exercises\myfile.txt"
count = 0
with open(fname, 'r') as f:
    for line in f:
        count += 1
print("Tổng số dòng là: ", count)
