"""
Tác giả: Lâm Quang Thắng
Ngày: 23/10/2021
Vấn đề:
 1. Gói phương pháp Newton để tính gần đúng căn bậc hai (Nghiên cứu điển hình 3.6) trong một
hàm có tên newton. Hàm này mong đợi số đầu vào là một đối số
và trả về ước lượng của căn bậc hai của nó. Tập lệnh cũng nên bao gồm một
chức năng cho phép người dùng tính căn bậc hai của đầu vào cho đến khi cô ấy nhấn
phím enter / return.

Giải pháp:
    ....
"""
import math
TOLERANCE=0.000001
def newton(x):
    estimate = 1.0
    while True:
        estimate = (estimate + x /estimate) /2
        difference = abs(x - estimate ** 2)
        if difference <= TOLERANCE:
            break
    return estimate


if __name__ == '__main__':
    while True:
        x = input("nhập một số dương hoặc enter / return để thoát: ")
        if x == "":
            break
        x = float(x)
        print("ước tính của chương trình là", newton(x))
        print("ước tính của python là   ", math.sqrt(x))

