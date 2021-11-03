"""
Author: Lâm Quang Thắng
Date: 25/09/2021
Program:
 Giả sử rằng một tệp chứa các số nguyên được phân tách bằng các dòng mới. Viết một đoạn mã
mở tệp và in giá trị trung bình của các số nguyên.

Solution:

    ....
"""

dem = 0
tong = 0
dau_vao_tep = open("T_B.txt", 'r')
for line in dau_vao_tep:
    tong += (line.strip())
    dem += 1
if dem == 0:
    trung_binh = 0
else:
    trung_binh = tong / dem
print("Mức trung bình là", trung_binh)
