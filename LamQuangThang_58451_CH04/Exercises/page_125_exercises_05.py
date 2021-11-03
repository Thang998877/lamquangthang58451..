"""
Author: Lâm Quang Thắng
Date: 25/09/2021
Program:
 Viết một đoạn mã nhắc người dùng nhập tên tệp. Nếu tệp tồn tại,
chương trình sẽ in nội dung của nó trên thiết bị đầu cuối. Nếu không, nó sẽ in một
thông báo lỗi.

Solution:

    ....
"""

tep = input("Nhập tên tệp: ")
try :
    a = open(tep)
except:
    print('Không thể mở tệp',tep ,'vui lòng thử lại')
    quit()
for line in a:
    line = line.upper()
    line = line.rstrip()
    print(line)
