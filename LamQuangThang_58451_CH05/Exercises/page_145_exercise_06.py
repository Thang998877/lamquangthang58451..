"""
Author: Lâm Quang Thắng
Date: 10/10/2021
Program: Viết một vòng lặp thay thế mỗi số trong danh sách có tên dữ liệu bằng giá trị tuyệt đối của nó.
Solution:
    ....
"""
data=[-2,-3,-6,-10,5,10]
processed = []
for number in data:
    if number < 0:
        processed.append(abs(number))
    else:
        processed.append(number)
print("Số ban đầu:\n", data)
print("Số đã xử lý:\n", processed)