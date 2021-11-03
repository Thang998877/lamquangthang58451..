"""
Author: Lâm Quang Thắng
Date: 23/09/2021
Program:
  Giả sử rằng biến myString tham chiếu đến một chuỗi. Viết một đoạn mã
sử dụng một vòng lặp để in các ký tự của chuỗi theo thứ tự ngược lại.

Solution:

    ....
"""
data = "myString"
b = ''
for i in range(1, len(data) + 1):
 b += data[-i]
 print(b)




