"""
Author: Lâm Quang Thắng
Date: 24/09/2021
Program:
  Giả sử rằng dữ liệu biến tham chiếu đến chuỗi "Python rules!". Sử dụng một chuỗi
phương pháp từ Bảng 4-2 để thực hiện các nhiệm vụ sau:
a. Lấy danh sách các từ trong chuỗi.
b. Chuyển chuỗi thành chữ hoa.
c. Xác định vị trí của chuỗi "Quy tắc".
d. Thay dấu chấm than bằng dấu chấm hỏi.
Solution:


    ....
"""
# a. Lấy danh sách các từ trong chuỗi.
a = "Python rules!"
print(len(a))
# b. Chuyển chuỗi thành chữ hoa.
a = "Python rules!"
print(a.upper())
# Xác định vị trí của chuỗi "rules".
a = "Python rules!"
print(a.find("rules"))
# Thay dấu chấm than bằng dấu chấm hỏi.
a = "Python rules!"
b = a.replace ("!", "?",)
print(b)