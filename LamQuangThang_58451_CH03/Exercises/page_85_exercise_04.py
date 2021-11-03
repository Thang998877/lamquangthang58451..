"""
Author: Lâm Quang Thắng
Date: 17/09/2021
Program:
   Giả sử rằng các biến x và y tham chiếu đến các chuỗi. Viết một đoạn mã để in
 các chuỗi này theo thứ tự bảng chữ cái. Bạn nên cho rằng chúng không bằng nhau.
Solution:

  ....
"""
x=input("Nhap chuoi x: ")
y=input("Nhap chuoi y: ")
words_x = [word.lower() for word in x.split()]
words_y = [word.lower() for word in y.split()]
words_x.sort()
words_y.sort()
print("Ki tu trong chuoi x la:  ")
for word1 in words_x:
    print(word1)
print("Ki tu trong chuoi y la:  ")
for word2 in words_y:
    print(word2)
