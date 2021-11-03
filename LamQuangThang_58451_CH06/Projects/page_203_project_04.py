"""
Tác giả: Lâm Quang Thắng
Ngày: 23/10/2021
Vấn đề:
 Cơ cấu lại phương pháp của Newton (Nghiên cứu điển hình 3.6) bằng cách phân tách nó thành ba
các chức năng hợp tác. Hàm newton có thể sử dụng chiến lược đệ quy
của Dự án 1 hoặc chiến lược lặp lại của Nghiên cứu điển hình 3.6. Nhiệm vụ kiểm tra
giới hạn được gán cho một hàm có tên là limitReached, trong khi nhiệm vụ tính toán một giá trị
gần đúng mới được gán cho một hàm có tên là advancedEstim. Mỗi
hàm mong đợi các đối số có liên quan và trả về một giá trị thích hợp.

Giải pháp:
    ....
"""
import math
tolerance = 0.000001

def newton(x, estimate=1):
    if limitreached(x, estimate):
        return estimate
    else:
        return newton(x, improveestimate(x, estimate))
def limitreached(x, estimate):
    difference = abs(x - estimate ** 2)
    return difference <= tolerance
def improveestimate(x, estimate):
    return (estimate + x / estimate) / 2
def main():
    while True:
        x = input("Nhập số dương hoặc enter/return để thoát:")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is: ", newton(x))
        print("Python's estimate is       ", math.sqrt(x))

main()
