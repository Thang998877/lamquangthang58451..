"""
Author: Lâm Quang Thắng
Date: 23/09/2021
Program:
Viết văn bản được mã hóa của mỗi từ sau đây bằng cách sử dụng mật mã Caesar với
giá trị khoảng cách là 3:
  a. python
  b. hacker
  c. wow
Solution:
 a. sbwkrq
 b. kdfnhu
 c. zrz

    ....
"""

"""
Mã hóa một chuỗi đầu vào gồm các chữ cái thường và bản in
kết quả. Đầu vào khác là giá trị khoảng cách
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


"""
Giải mã chuỗi đầu vào gồm các chữ cái thường và bản in
kết quả. Đầu vào khác là giá trị khoảng cách.
"""
ma = input("Nhập văn bản được mã hóa: ")
khoan_cach = int(input("Nhập giá trị khoảng cách: "))
van_ban_tho = ""
for ch in ma:
 gia_tri = ord(ch)
 mat_ma = gia_tri - khoan_cach
 if mat_ma < ord('a'):
     mat_ma= ord('z') - \
                 (khoan_cach - (ord('a') - gia_tri - 1))
     print(ch, "|", gia_tri, "->", chr(mat_ma), "|", mat_ma)
 van_ban_tho += chr(mat_ma)
print(van_ban_tho)