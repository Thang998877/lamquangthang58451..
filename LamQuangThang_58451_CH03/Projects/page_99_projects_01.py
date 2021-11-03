"""
Author: Lâm Quang Thắng
Date: 17/09/2021
Program:
   Viết chương trình nhận độ dài ba cạnh của tam giác làm đầu vào.
Kết quả đầu ra của chương trình phải cho biết tam giác có phải là cạnh đều hay không.

Solution:
    ....
"""
a, b, c = input("Nhập 3 cạnh của tam giác: ").split()
a, b, c = float(a), float(b), float(c)
if a + b > c and a + c > b and b + c > a:
    tamgiac = ""
    if a == b == c:
        tamgiac = "deu"
    print(str(a) + ", " + str(b) + ", " + str(c) + " la ba canh cua tam giac " + tamgiac)
else:
    print("Khong phai tam giac đeu")