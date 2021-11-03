"""
Author: Lâm Quang Thắng
Date: 18/09/2021
Program:
  Ước chung lớn nhất của hai số nguyên dương A và B là ước lớn nhất
số có thể được chia đều cho cả hai người trong số họ. Thuật toán của Euclid có thể
được sử dụng để tìm ước chung lớn nhất (GCD) của hai số nguyên dương. Bạn
có thể sử dụng thuật toán này theo cách sau:
Một. Tính phần còn lại của phép chia số lớn hơn cho số nhỏ hơn
con số.
NS. Thay số lớn hơn bằng số nhỏ hơn và số nhỏ hơn
với phần còn lại.
NS. Lặp lại quá trình này cho đến khi số nhỏ hơn bằng 0. Số lớn hơn tại thời điểm này là GCD của A và B. Viết chương trình cho phép
người dùng nhập hai số nguyên và sau đó in từng bước trong quá trình sử dụng
Thuật toán Euclid để tìm GCD của chúng.

Solution:
    ....
"""
#xác định hàm tính toán GCD
def EuclideanGCD(A,B):
    if A < B:
        A , B = B , A

    #điều kiện cơ bản.
    if(A % B) == 0:
        return B

    #cuộc gọi đệ qui.python page_100_projects_08.py
    else:
        T = A % B
        return (EuclideanGCD(B,T))
#nhập các số.
A = int(input('nhập số đầu tiên: '))
B = int(input('nhập số thứ hai: '))
#in GDC
print('GDC: ', EuclideanGCD(A,B))

