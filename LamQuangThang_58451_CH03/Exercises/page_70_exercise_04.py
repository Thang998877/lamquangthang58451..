"""
Author: Lâm Quang Thắng
Date: 15/09/2021
Program:
Viết một vòng lặp in 128 giá trị ASCII đầu tiên theo sau là giá trị tương ứng
các ký tự (xem phần về các ký tự trong Chương 2). Cần biết rằng hầu hết các
Giá trị ASCII trong phạm vi “0..31” thuộc về các ký tự điều khiển đặc biệt không có biểu diễn in stan dard, vì vậy bạn có thể thấy các ký hiệu lạ trong đầu ra cho các ký tự này
các giá trị.
Solution:

    ....
"""
for I in range(128):
    gia_tri = ascii(I)
    ki_hieu = chr(I)
    print(ki_hieu,end=" ")
    print(gia_tri,end=" ")
