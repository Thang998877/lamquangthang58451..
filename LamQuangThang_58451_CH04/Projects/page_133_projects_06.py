"""
Author: Lâm Quang Thắng
Date: 24/09/2021
Program:
 Sử dụng chiến lược chuyển đổi từ thập phân sang nhị phân và toán hạng sang trái dịch chuyển bit được xác định trong Dự án 5 để mã hóa một thuật toán mã hóa mới. Thuật toán
nên thêm 1 vào giá trị ASCII bằng số của mỗi ký tự, chuyển đổi nó thành một chuỗi bit,
và dịch chuyển các bit của chuỗi này sang trái một chỗ. Một ký tự khoảng trắng trong
chuỗi mã hóa phân tách các chuỗi bit kết quả.
Solution:

    ....
"""
#chuyển đổi int sang nhị phân
def binary_string(num):
    bit_strng="{0:b}".format(num);
    return bit_strng

#lấy chuỗi làm đầu vào từ người dùng
str=input("Nhập một chuỗi: ")
bit_list = []
for i in str:
    bits = binary_string(ord(i)+1)
    bits = bits[1:]+bits[0]
    bit_list.append(bits)
output = ""
#hiển thị kết quả
for bit in bit_list:
    output += bit + " "
print(output)
