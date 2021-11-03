"""
Author: Lâm Quang Thắng
Date: 23/09/2021
Program:
  Giả sử rằng biến myString tham chiếu đến một chuỗi và biến
reverseString đề cập đến một chuỗi rỗng. Viết một vòng lặp có thêm các ký tự
từ myString đến reverseString theo thứ tự ngược lại.

Solution:

    ....
"""

myString = input(str("Nhập chuỗi của bạn : "))
reversedString = ''
l = len(myString) - 1
while l >= 0:
    reversedString += myString[l]
    l = l - 1
print(reversedString)