"""
Author: Lâm Quang Thắng
Date: 05/10/2021
Program:
  Viết chương trình cho phép người dùng điều hướng các dòng văn bản trong tệp. Các
chương trình sẽ nhắc người dùng nhập tên tệp và nhập các dòng văn bản vào
danh sách. Sau đó, chương trình đi vào một vòng lặp trong đó nó in ra số dòng trong
và nhắc người dùng nhập số dòng. Số dòng thực tế nằm trong khoảng từ 1 đến
số dòng trong tệp. Nếu đầu vào là 0, chương trình sẽ thoát. Nếu không
chương trình in dòng liên kết với số đó.

Solution:

    ....
"""

enterfile = input("Nhập tên tệp: ")
file = open(enterfile, 'r')
linecount = 0
for line in file:
    linecount = linecount + 1
print("Số dòng trong txt này. tập tin là", linecount)
while True:
    linenum = 0
    num = int(input("Vui lòng nhập số dòng hoặc nhấn 0 để thoát: "))
    if num >=1 and num <= linecount:
        file = open(enterfile, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(lines)
    else:
        if num == 0:
            print("Cảm ơn vì đã sử dụng chương trình")
            break

