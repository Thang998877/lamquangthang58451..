"""
Author: Lâm Quang Thắng
Date: 25/09/2021
Program:

Solution:

    ....
"""
van_ban_tho = input("Nhập tin nhắn một từ, viết thường: ")
khoang_cach = int(input("Nhập giá trị khoảng cách: "))
code = ""
for ch in van_ban_tho:
 gia_tri = ord(ch)
 mat_ma = gia_tri + khoang_cach
 if mat_ma > ord('z'):
   mat_ma = ord('a') + khoang_cach - \
                (ord('z') -gia_tri+ 1)
 print(ch,"|",gia_tri, "->", chr(mat_ma), "|", mat_ma)
 code += chr(mat_ma)
print(code)
