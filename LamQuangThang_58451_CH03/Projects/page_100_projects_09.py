"""
Author: Lâm Quang Thắng
Date: 18/09/2021
Program:
  Viết một chương trình nhận một chuỗi số từ người dùng và cho phép
người dùng nhấn phím enter để cho biết rằng họ đã hoàn tất việc cung cấp đầu vào.
Sau khi người dùng nhấn phím enter, chương trình sẽ in ra tổng
số và giá trị trung bình của chúng.

Solution:
    ....
"""
numbers = []
print("nhấn enter 2 lần để dừng lại")
while(True):
    a = input("Nhập một số: ")
    if a:
        numbers.append(int(a))
    elif(a == ''):
            break
b =0
for a in numbers:
    b += a
avg = b / len(numbers)
print(b)
print(avg)