"""
Tác giả: Lâm Quang Thắng
Ngày: 23/10/2021
Vấn đề:
  Chuyển đổi phương pháp của Newton để tính gần đúng căn bậc hai trong Dự án 1 thành một hàm sive định kỳ có tên newton.
(Gợi ý: Ước lượng của căn bậc hai phải là
được truyền dưới dạng đối số thứ hai cho hàm.)

Giải pháp:
    ....
"""
import math
TOLERANCE = 0.000001

def newton(x, estimate):
        difference = abs(x - estimate ** 2)
        if difference <= TOLERANCE:
          return estimate
        else:
            return estimate(x, (estimate + x / estimate)/2)


def main():
    while True:
        x = input("nhập một số dương hoặc enter / return để thoát: ")
        if x == "":
            break
        x = float(x)
        print("ước tính của chương trình là", newton(x, 1))
        print("ước tính của python là   ", math.sqrt(x))
main()

