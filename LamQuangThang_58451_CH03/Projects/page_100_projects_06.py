"""
Author: Lâm Quang Thắng
Date: 18/09/2021
Program:
   Nhà toán học người Đức Gottfried Leibniz đã phát triển phương pháp sau
để gần đúng giá trị của π:
π / 4 5 1] 1/3 1 1/5] 1/7 1. . .
Viết một chương trình cho phép người dùng chỉ định số lần lặp được sử dụng trong
ước tính này và hiển thị giá trị kết quả.

Solution:
    ....
"""
lap_lai = int(input("Nhập số lần lặp lại: "))
list01 = []
list02 = []
y = 1
# in số (number)
for x in range(1, lap_lai + 1):
    number = (1.0 / y)
    list01.append(number)
    y += 2.0
# in phủ định (neg)
for i in range(1, lap_lai, 2):
    neg = list01[i] * -1.0
    list02.append(neg)

comb = (sum(list01)) + (sum(list02)) + (sum(list02))
pi = comb * 4.0
print("Giá trị gần đúng của pi là", pi)