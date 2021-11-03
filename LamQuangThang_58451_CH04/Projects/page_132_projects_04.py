"""
Author: Lâm Quang Thắng
Date: 24/09/2021
Program:
 Các số bát phân có cơ số là tám và các chữ số 0-7. Viết các tập lệnh octalTo Decimal.py và decimalToOctal.py,
các tập lệnh này chuyển đổi các số giữa các bát phân
và biểu diễn thập phân của số nguyên. Các tập lệnh này sử dụng các thuật toán
tương tự như các tập lệnh binaryToDecimal và decimalToBinary được phát triển trong Phần 4-3.
Solution:

    ....
"""

# Đầu vào
o_t_n=int(input('Nhập một chuỗi các chữ số bát phân: '))
# các biến bắt buộc
i = 1
dc = 0
# vòng lặp chuyển đổi
while (o_t_n != 0):
    #để tìm phần còn lại
    rmd = o_t_n % 10
    o_t_n //= 10
    dc += rmd * i
    i *= 8
#in kết quả
print('Giá trị số nguyên là: ',dc)
# decimalToOctal.py
# in
d_c_n=int(input('Nhập một số nguyên thập phân: '))
print("Thương số còn lại Octal")
#các biến bắt buộc
i = 1
o_c_n = 0
num = ""
#vòng lặp chuyển đổi
while (d_c_n != 0):
    # để tìm phần còn lại
    rm = d_c_n % 8
    d_c_n //= 8
    o_c_n = o_c_n + rm * i
    i *= 10
    num = str(rm)+num
    print("%5d%8d%12s" % (d_c_n, rm, num))
#in kết quả
print('Biểu diễn bát phân là ',o_c_n)

