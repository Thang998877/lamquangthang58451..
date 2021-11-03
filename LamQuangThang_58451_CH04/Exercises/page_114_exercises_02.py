"""
Author: Lâm Quang Thắng
Date: 24/09/2021
Program:
  Dịch từng số sau sang số nhị phân:
a. 4710
b. 12710
c. 6410

Solution:

a.  1001001100110
b.  11000110100110
c.  1100100001010

    ....
"""

"""
Chuyển đổi một số nguyên thập phân thành số nhị phân
"""
so_thap_phan = int(input("Nhập một số nguyên thập phân: "))
if so_thap_phan == 0:
 print(0)
else:
 print("Thương số còn lại nhị phân")
 nhi_phan = ""
 while so_thap_phan > 0:
  con_lai = so_thap_phan % 2
  so_thap_phan = so_thap_phan // 2
  nhi_phan = str(con_lai) + nhi_phan
  print("%5d%8d%12s" % (so_thap_phan, con_lai ,nhi_phan))
  print("Biểu diễn nhị phân là", nhi_phan)

