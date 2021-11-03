"""
Author: Lâm Quang Thắng
Date: 24/09/2021
Program:
  Viết tập lệnh nhập một dòng văn bản được mã hóa và giá trị khoảng cách và kết quả đầu ra
bản rõ sử dụng mật mã Caesar. Tập lệnh sẽ hoạt động với mọi ký tự có thể in được.
Solution:

    ....
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