"""
Author: Lâm Quang Thắng
Date: 24/09/2021
Program:
Viết một tập lệnh nhập vào một dòng văn bản rõ và một giá trị khoảng cách và xuất ra một
văn bản được mã hóa bằng mật mã Caesar. Tập lệnh sẽ hoạt động cho bất kỳ bản in nào
nhân vật.

Solution:
    ....
"""
# Nhắc người dùng nhập văn bản được mã hóa
ma_hoa = input("nhập văn bản được mã hóa ")
# Nhắc người dùng nhập khoảng cách
khoang_cach = int(input("nhập giá trị khoảng cách: "))
van_ban_tho = ""
#Logic để mã hóa
for ch in ma_hoa:
  # ord trả về giá trị int cho unicode
  gia_tri = ord(ch)
  mat_ma = gia_tri - khoang_cach
  if mat_ma < ord('a'):
    mat_ma = ord('z') - \
      (khoang_cach - (ord('a') - gia_tri - 1))
  van_ban_tho += chr(mat_ma)
# In văn bản được mã hóa
print(van_ban_tho)