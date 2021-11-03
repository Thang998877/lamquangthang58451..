"""
Author: Lâm Quang Thắng
Date: 25/09/2021
Program:
 Viết một tập lệnh có tên numberlines.py. Tập lệnh này tạo một danh sách chương trình từ một
chương trình nguồn. Tập lệnh này sẽ nhắc người dùng về tên của hai tệp. Các
tên tệp đầu vào có thể là tên của chính tập lệnh, nhưng hãy cẩn thận sử dụng
tên tệp xuất ra! Tập lệnh sao chép các dòng văn bản từ tệp đầu vào sang đầu ra
tệp, đánh số từng dòng khi nó đi. Các số dòng phải được căn phải trong
4 cột, để định dạng của một dòng trong tệp đầu ra giống như ví dụ sau:
1> Đây là dòng đầu tiên của văn bản.

Solution:

    ....
"""

input_filename = input ('Nhập tên tập tin đầu vào:')
output_filename = input ('Nhập tên tập tin đầu ra:')

f = open (input_filename, 'r'),
w = open (output_filename, 'w')
so = 0
dong = 1
w.write('{:> 4}> {}'. format(so, dong))


