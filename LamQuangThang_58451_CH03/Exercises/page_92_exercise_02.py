"""
Author: Lâm Quang Thắng
Date: 16/09/2021
Program:
Giai thừa của một số nguyên N là tích của các số nguyên từ 1 đến N, inclu sive. Viết một vòng lặp while tính giai thừa của một số nguyên cho trước
Solution:

    ....
"""


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

num = 5;
print("Factorial of", num, "is",
      factorial(num))