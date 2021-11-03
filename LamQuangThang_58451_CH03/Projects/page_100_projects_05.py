"""
Author: Lâm Quang Thắng
Date: 18/09/2021
Program:
 Một nhà sinh vật học địa phương cần một chương trình để dự đoán sự gia tăng dân số. Các đầu vào
sẽ là số lượng sinh vật ban đầu, tốc độ phát triển (một số thực
lớn hơn 0), số giờ cần để đạt được tốc độ này và một số
số giờ trong đó dân số tăng lên. Ví dụ: một người có thể bắt đầu bằng
quần thể 500 sinh vật, tốc độ tăng trưởng là 2 và thời kỳ tăng trưởng cần đạt được
tỷ lệ này trong 6 giờ. Giả sử rằng không có sinh vật nào chết, điều này có nghĩa là
rằng dân số này sẽ tăng gấp đôi sau mỗi 6 giờ. Vì vậy, sau khi cho phép
6 giờ để tăng trưởng, chúng tôi sẽ có 1000 sinh vật và sau 12 giờ, chúng tôi sẽ
có 2000 sinh vật. Viết một chương trình lấy các đầu vào này và hiển thị một phần trước của tổng dân số.
Solution:
    ....
"""
sinh_vat = int(input("Nhập số lượng sinh vật ban đầu:"))
ti_le_tang_truong = int(input("Nhập tốc độ tăng trưởng [một số thực> 0] : "))
gio_tang_truong = int(input("Nhập số giờ để đạt được tốc độ tăng trưởng: "))
tong_gio_tang_truong = int(input("Nhập tổng số giờ tăng trưởng: "))
gio = 0
while (gio <= tong_gio_tang_truong):
    sinh_vat*=ti_le_tang_truong
    gio += gio_tang_truong
    if (gio==tong_gio_tang_truong):
        break
print("Tổng dân số là:" ,sinh_vat)