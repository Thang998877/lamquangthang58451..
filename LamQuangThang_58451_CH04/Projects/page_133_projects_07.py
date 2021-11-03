"""
Author: Lâm Quang Thắng
Date: 24/09/2021
Program:
  Viết một tập lệnh giải mã một thông điệp được mã hóa bằng phương pháp được sử dụng trong Dự án 6.
Solution:

    ....
"""

message = input("Enter the coded text: ")
decimal = 0
exponent = len(message) - 1
bString = ""
for digit in message.split():
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
    bString += chr(int(digit, 2))
print(bString)

