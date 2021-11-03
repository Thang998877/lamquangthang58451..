"""
Author: Lâm Quang Thắng
Date: 24/09/2021
Program:
   Dịch chuyển bit là một thủ tục theo đó các bit trong một chuỗi bit được di chuyển sang trái hoặc
rẽ phải. Ví dụ: chúng ta có thể chuyển các bit trong chuỗi 1011 hai vị trí thành
bên trái để tạo ra chuỗi 1110. Lưu ý rằng hai bit ngoài cùng bên trái được quấn quanh phía bên phải của chuỗi trong thao tác này.
Xác định hai tập lệnh,
shiftLeft.py và shiftRight.py, mong đợi một chuỗi bit làm đầu vào. Kịch bản
shiftLeft dịch chuyển các bit trong đầu vào của nó sang một chỗ sang trái, bao bọc bit ngoài cùng bên trái
đến vị trí ngoài cùng bên phải. Script shiftRight thực hiện thao tác nghịch đảo.
Mỗi tập lệnh in ra chuỗi kết quả.
Solution:

    ....
"""

#Thực hiện phương pháp shiftLeft
#thay đổi các bit trong đầu vào của nó
#đặt bên trái
def shiftLeft(bitstring):
    bitstring = bitstring[1:]+bitstring[0]
    #trả về dưới dạng định dạng chuỗi bit
    return bitstring
#Nhận thông tin đầu vào từ người dùng
bits = input("Nhập một chuỗi bit: ")
#gọi phương thức shiftLeft trả về giá trị
# được lưu trữ trong leftShift
leftShift = shiftLeft(bits)
#Hiển thị đầu ra
print()
print(leftShift)
print()
