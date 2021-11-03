"""
Author: Lâm Quang Thắng
Date: 06/09/2021
Program:
Write a string that contains your name and address on separate lines using embedded newline characters. Then write the same string literal without the newline
characters.
Solution:
    ....
"""
#with newline character
name = "Lâm Quang Thắng"
address = "Da Nang"
Inthongtin= "Bạn tên là %s \nDia chi  %s"%(name,address)
print(Inthongtin)
#without newline charater
name = "Lâm Quang Thắng"
address = "Da Nang"
Inten="bạn tên là: %s"%name
Indiachi="Dia chi cua ban : %s"%address
print(Inten)
print(Indiachi)