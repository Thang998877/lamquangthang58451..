"""
Author: Lâm Quang Thắng
Date: 25/09/2021
Program:
 Viết một tập lệnh có tên copyfile.py. Tập lệnh này sẽ nhắc người dùng về
tên của hai tệp văn bản. Nội dung của tệp đầu tiên phải được nhập và viết
đến tệp thứ hai.

Solution:

    ....
"""

# để nhắc người dùng nhập tệp 1 là tệp đầu vào
file1 = input("nhập tên tệp đầu vào có phần mở rộng : ")
# để nhắc người dùng nhập tệp 2 là tệp đầu ra
file2 = input("nhập tên tệp đầu ra có phần mở rộng : ")
# mở tệp1 ở chế độ đọc
fn1 = open(file1, 'r')
# mở tệp2 ở chế độ đầu ra
fn2 = open(file2, 'w')
# đọc nội dung của từng dòng tệp
cont = fn1.readlines()
# loại (tiếp)
for i in range(0, len(cont)):
    fn2.write(cont[i])
# đóng tập tin
fn2.close()
print("Nội dung của tệp đầu tiên được sao chép sang tệp thứ hai")
# mở tệp ở chế độ đọc
fn2 = open(file2, 'r')
# đọc nội dung của tập tin
cont1 = fn2.read()
# in nội dung của tập tin
print("Nội dung của tệp thứ hai: ")
print(cont1)
# đóng tất cả các tệp
fn1.close()
fn2.close()
