"""
Author: Lâm Quang Thắng
Date: 25/09/2021
Program:
 Viết một tập lệnh có tên là dif.py. Tập lệnh này sẽ nhắc người dùng về tên
của hai tệp văn bản và so sánh nội dung của hai tệp để xem chúng có phải là
tương tự. Nếu đúng như vậy, tập lệnh sẽ chỉ xuất ra "Có". Nếu không, kịch bản
sẽ xuất ra "Không", theo sau là các dòng đầu tiên của mỗi tệp khác với mỗi
khác. Vòng lặp đầu vào nên đọc và so sánh các dòng từ mỗi tệp. Vòng lặp
nên ngắt ngay khi tìm thấy một cặp đường thẳng khác nhau.
Solution:

    ....
"""


# xác định biến f1 nhập tệp 1
f1 = input('Nhập tên tệp đầu tiên: ')
# xác định biến f2 nhập vào tệp 2
f2 = input('Nhập tên tệp thứ hai: ')
# xác định biến file1 mở các tệp đầu tiên bằng cách sử dụng phương thức mở
file1 = open(f1, 'r')
# xác định biến file1 mở tệp thứ hai bằng cách sử dụng phương thức mở
file2 = open(f2, 'r')
# xác định biến d1 sử dụng phương thức readlines để đọc dữ liệu tệp đầu tiên
d1 = file1.readlines()
# xác định biến d2 sử dụng phương thức readlines để đọc dữ liệu tệp thứ hai
d2 = file2.readlines()
#defining if block kiểm tra dữ liệu tệp
if d1 == d2:
 # khi giá trị được khớp nó sẽ in ra thông báo có
  print ('có')
 # sử dụng từ khóa exit để thoát khỏi khối if
exit
# xác định vòng lặp for lưu trữ độ dài của tệp
for j in range (0, min (len (d1), len (d2))):
 # xác định nếu khối mà giá trị kiểm tra không khớp
    if (d1[j]!=d2[j]):
# in ra thông báo "KHÔNG"
      print ('không')
# giá trị tệp in
      print ("các giá trị không khớp:", d1[j], "", d2[j])

