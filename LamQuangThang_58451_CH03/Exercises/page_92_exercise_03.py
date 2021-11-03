"""
Author: Lâm Quang Thắng
Date: 17/09/2021
Program:
 Log 2 của một số N cho trước được M cho trong phương trình N 5 2M. Sử dụng số nguyên
cấp số cộng, giá trị của M xấp xỉ bằng số lần N có thể là
chia đều cho 2 cho đến khi nó trở thành 0. Viết một vòng lặp tính toán xấp xỉ này của log 2 của một số nhất định N.
Bạn có thể kiểm tra mã của mình bằng cách nhập
hàm math.log và đánh giá vòng biểu thức (math.log (N, 2)) (lưu ý
rằng hàm math.log trả về một giá trị dấu phẩy động).

Solution:
  ....
"""

import math
n=int(input("Nhap n: "))

for m in range(1):
    print("Logarit cua",n,"la: ", round(math.log( n , 2)))