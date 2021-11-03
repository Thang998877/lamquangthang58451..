"""
Author: Lâm Quang Thắng
Date: 18/09/2021
Program:
   Giáo viên ở hầu hết các khu học chánh được trả lương theo lịch trình
 dựa trên số năm kinh nghiệm giảng dạy của họ. Ví dụ, một sự khởi đầu
 giáo viên trong Học khu Lexington có thể được trả $ 30.000 trong năm đầu tiên. Vì
  mỗi năm kinh nghiệm sau năm đầu tiên này, tối đa 10 năm, giáo viên nhận được
 Tăng 2% so với giá trị trước đó. Viết chương trình hiển thị bảng lương, ở định dạng bảng,
 dành cho giáo viên trong một khu học chánh. Các đầu vào là khởi đầu
 lương, tỷ lệ phần trăm tăng và số năm trong lịch trình. Từng hàng
 trong lịch trình phải có số năm và mức lương của năm đó.

Solution:
    ....
"""
lương_khoi_diem = float(input("Nhập mức lương khởi điểm: "))

phan_tram_hang_nam = (int(input("Nhập % tăng hàng năm: ")) / 100)

kinh_nghiem = int(input("nhập số năm kinh nghiệm: "))

for count in range(1, kinh_nghiem + 1):
    print("Year ", count, " Salary: ", lương_khoi_diem * ((1 + phan_tram_hang_nam ) ** (count - 1)))