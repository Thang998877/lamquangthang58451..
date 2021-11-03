"""
Author: Lâm Quang Thắng
Date: 25/09/2021
Program:
 Bộ phận tính lương lưu giữ danh sách thông tin nhân viên cho mỗi kỳ trả lương
trong một tệp văn bản. Định dạng của mỗi dòng của tệp như sau:
<họ> <lương theo giờ> <giờ làm>
Viết chương trình nhập tên tệp từ người dùng và in ra thiết bị đầu cuối a
báo cáo về tiền lương đã trả cho người lao động trong thời gian nhất định. Báo cáo nên
ở định dạng bảng với tiêu đề thích hợp. Mỗi dòng phải chứa một
tên của nhân viên, số giờ làm việc và tiền lương được trả cho khoảng thời gian đó
Solution:

    ....
"""
file_name = input('Nhập tên tập tin đầu vào:')
# in tiêu đề trên thiết bị đầu cuối
print('\ n% -15s% -10s% -10s'% ('Tên', 'Giờ', 'Tổng thanh toán'))
# mở tệp và lặp lại từng dòng
for line in open(file_name):
       line = line.strip()
    # nếu dòng không trống
       if line != '':
        # tách dòng và bắt từng nhóm
        (nm, wage, hours) = line.split()
        # tên nằm trong chuỗi, trong khi tiền lương và giờ tiếp theo
        # được chuyển đổi dạng sting thành float
        wage = float(wage)
        hours = float(hours)
        pay = wage * hours
        print('% - 15s% -10d% -10.2f' % (nm, hours, pay))



