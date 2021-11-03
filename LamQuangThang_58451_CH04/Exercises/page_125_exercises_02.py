"""
Author: Lâm Quang Thắng
Date: 25/09/2021
Program:
 Viết một đoạn mã để mở một tệp để nhập và in ra số
các từ gồm bốn chữ cái trong tệp
Solution:

    ....
"""
file = input("nhập file cần tìm ")
input = open(file, 'r')
chu = input . read()
tu = len(chu . split())
if str(tu) == 4:
    print("số thú tự có 4 chữ cái là: ", tu)

