"""
Tác giả: Lâm Quang Thắng
Ngày: 23/10/2021
Vấn đề:
 Elena phàn nàn rằng hàm newton đệ quy trong Dự án 2 bao gồm một
đối số cho ước tính. Người dùng của chức năng không cần phải cung cấp
giá trị, luôn luôn giống nhau, khi họ gọi hàm này. Sửa đổi định nghĩa của hàm để nó sử dụng đối số từ khóa với
giá trị mặc định và gọi hàm mà không có đối số thứ hai để chứng minh
rằng nó giải quyết vấn đề này
Giải pháp:
    ....
"""
import math
tolerance = 0.000001

def newton(x, estimate=1):
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        return newton(x, (estimate + x / estimate /2))
def main():
    while True:
        x = input("Nhập số dương hoặc enter/return để thoát:")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is: ", newton(x))
        print("Python's estimate is       ", math.sqrt(x))

main()