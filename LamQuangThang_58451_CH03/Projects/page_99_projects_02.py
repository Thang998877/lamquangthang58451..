"""
Author: Lâm Quang Thắng
Date: 17/09/2021
Program:
   Viết chương trình nhận độ dài ba cạnh của tam giác làm đầu vào.
Kết quả đầu ra của chương trình sẽ cho biết tam giác có phải là góc vuông hay không.
Nhắc lại định lý Pitago rằng trong một tam giác vuông, bình phương của
một cạnh bằng tổng bình phương của hai cạnh còn lại.

Solution:
    ....
"""
a, b, c = map(float, input('nhập 3 số cần kiểm tra: ').split())
if a+b>c and b+c>a and c+a>b:
    if a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
        print('đây là ba cạnh của tam giác vuông')
else:
     print('đây không phải ba cạnh của tam giác vuông')