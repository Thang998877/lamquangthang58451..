"""
Author: Lâm Quang Thắng
Date: 17/09/2021
Program:
 Một thí nghiệm khoa học tiêu chuẩn là thả một quả bóng và xem nó nảy lên cao đến mức nào.
Khi “độ nảy” của quả bóng đã được xác định, tỷ số này sẽ đưa ra chỉ số bounci ness.
Ví dụ, nếu một quả bóng rơi từ độ cao 10 feet sẽ nảy lên 6 feet
cao, chỉ số 0,6 và tổng quãng đường bóng đi được là 16 feet sau
một lần trả lại. Nếu quả bóng tiếp tục nảy, khoảng cách sau hai lần nảy sẽ là 10 ft 6 111 ft 6 ft 3,6 ft 5 25,6 ft.
Lưu ý rằng khoảng cách di chuyển cho
mỗi lần trả lại liên tiếp là khoảng cách đến sàn cộng với 0,6 của khoảng cách đó là
bóng quay trở lại. Viết chương trình cho phép người dùng nhập chiều cao ban đầu
từ đó thả bóng và số lần thả bóng
tiếp tục nảy. Đầu ra phải là tổng quãng đường bóng đi được.
 a: chiều cao
 b: lần nảy
 c: độ nảy
 d: hệ số nảy

Solution:
    ....
"""
a = int(input("Nhap chieu cao ban dau: "))
b = int(input("Nhap so lan bong nay: "))
c = int(input("Nhap do nay cua bong: "))
d = c/a
print("He so nay cua bong la: ", d)
total = float()
if b == 1:
    total = a+c
    print("Quang duong bong di duoc sau lan nay thu 1 la: ", total)
else:
    total = a+(c*b)+(c*b*d)
    print("Quang duong bong di duoc sau lan nay thu 2 la: ", total)