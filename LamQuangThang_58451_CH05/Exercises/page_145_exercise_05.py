"""
Author: Lâm Quang Thắng
Date: 10/10/2021
Program: Giả sử rằng dữ liệu đề cập đến một danh sách các số và kết quả đề cập đến một danh sách trống.
Viết một vòng lặp để thêm các giá trị khác không trong dữ liệu vào danh sách kết quả, giữ chúng
ở các vị trí tương đối của chúng và loại trừ các số không.
Solution:
    ....
"""
data = [35,90,67,89,102]
result = ""
for number in data:
   if number != 0:
       result += str(number)
