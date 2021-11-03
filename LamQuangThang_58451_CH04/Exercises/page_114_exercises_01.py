"""
Author: Lâm Quang Thắng
Date: 24/09/2021
Program:
   Dịch từng số sau sang số thập phân:
a. 110012
b. 1000002
c. 111112

Solution:
 a. 52
 b. 66
 c. 64

    ....
"""

"""
Chuyển đổi số nhị phân thành số nguyên thập phân.
"""
nhi_phan = input("Nhập một chuỗi bit: ")
so_thap_phan = 0
so_mu = len(nhi_phan) - 1
for chu_so in nhi_phan:
 so_thap_phan = so_thap_phan + int(chu_so) * 2 ** so_mu
 so_mu = so_mu - 1
print("Giá trị số nguyên là: ", so_thap_phan)

