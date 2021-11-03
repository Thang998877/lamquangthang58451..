"""
Author: Lâm Quang Thắng
Date: 10/10/2021
Program:
 Xác định một hàm có tên là tổng kết. Hàm này mong đợi hai số, được đặt tên là
thấp và cao, như các đối số. Hàm tính toán và trả về tổng của
con số giữa thấp và cao, bao gồm.

Solution:
    ....
"""
lower = int(input("Nhập giới hạn dưới: "))
upper = int(input("Nhập giới hạn trên: "))
the_sum = 0
for number in range(lower, upper + 1):
    the_sum = the_sum + number
    print(the_sum)
