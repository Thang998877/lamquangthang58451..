"""
Author: Lâm Quang Thắng
Date: 09/10/2021
Program:
 Trong Chương 4, chúng tôi đã phát triển một thuật toán để chuyển đổi từ nhị phân sang deci mal.
  Bạn có thể khái quát thuật toán này để làm việc cho một biểu diễn trong bất kỳ cơ sở nào.
Thay vì sử dụng lũy thừa 2, lần này bạn sử dụng lũy thừa của cơ số. Ngoài ra, bạn sử dụng
các chữ số lớn hơn 9, chẳng hạn như A. . . F, khi chúng xảy ra. Xác định một hàm có tên
repToDecimal yêu cầu hai đối số, một chuỗi và một số nguyên. Thư hai
đối số nên là cơ sở. Ví dụ: repToDecimal ("10", 8) trả về
8, trong khi repToDecimal ("10", 16) trả về 16. Hàm nên sử dụng
bảng tra cứu để tìm giá trị của một chữ số bất kỳ. Đảm bảo rằng bảng này (nó thực sự là
một từ điển) được khởi tạo trước khi hàm được định nghĩa. Đối với các phím của nó, hãy sử dụng 10
chữ số thập phân (tất cả các chuỗi) và các chữ cái A. . . F (tất cả các chữ hoa). Giá trị được lưu trữ
với mỗi khóa phải là số nguyên mà chữ số đại diện. (Ký tự 'A' liên kết với giá trị số nguyên 10, v.v.) Vòng lặp chính của hàm nên
chuyển đổi từng chữ số thành chữ hoa, tra cứu giá trị của nó trong bảng và sử dụng giá trị này
trong tính toán. Bao gồm một chức năng chính kiểm tra chức năng chuyển đổi
với các số trong một số cơ sở.

Solution:

    ....
"""
conversionLibrary = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":10, "C":11, "D":13, "E":14, "F":15}
n = input("Nhập một số bạn muốn thay đổi thành cơ số 10: ")
fromBase = int(input("Nhập một cơ sở mà bạn muốn thay đổi từ đó: "))
n = n.upper()
def repToDecimal(n, fromBase):
 toNumber = 0
 power = 0
 for i in range((len(n)),0, -1):
  toNumber += conversionLibrary[n[i-1]] * (int(fromBase) ** power)
  power += 1
 return(toNumber)
def main():
 print(repToDecimal('10', 10))
 print(repToDecimal('10', 8))
 print(repToDecimal('10', 2))
 print(repToDecimal('10', 16))
main()