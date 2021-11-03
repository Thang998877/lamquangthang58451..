"""
Author: Lâm Quang Thắng
Date: 16/09/2021
Program:
  Giả sử rằng x là một số. Viết một đoạn mã in số
giá trị tuyệt đối mà không cần sử dụng hàm abs của Python.
Solution:
    ....
"""
x = 8
def getAbs(n):
    mask = n >> (x - 1)
    return ((n + mask) ^ mask)
n = -8
print("giá trị tuyệt đối của", n, "là", getAbs(n))