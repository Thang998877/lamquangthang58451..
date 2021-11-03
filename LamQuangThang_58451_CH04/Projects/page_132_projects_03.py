"""
Author: Lâm Quang Thắng
Date: 24/09/2021
Program:
  Sửa đổi các tập lệnh của Dự án 1 và 2 để mã hóa và giải mã toàn bộ tệp văn bản
Solution:

    ....
"""
inputFile = input("Nhập tên tệp đầu vào: ")
outputFile = input("Nhập tên tệp đầu ra: ")
dist = int(input("Nhập giá trị khoảng cách: "))
infile = open(inputFile, "r")
outfile = open(outputFile, "w")
get = infile.readlines()
for text in get:
    code = ""
for char in text:
    Value = ord(char)
    cipher = Value + dist
    f = cipher > 127
cipher = dist - (127 - Value | 1)
code += chr (cipher)
outfile.write(code)
