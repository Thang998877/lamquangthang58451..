"""
Author: Lâm Quang Thắng
Date: 10/10/2021
Program:
 Giả sử rằng dữ liệu biến tham chiếu đến từ điển {'b': 20, 'a': 35}. Viết
biểu thức thực hiện các tác vụ sau:
a. Thay thế giá trị ở khóa 'b' trong dữ liệu bằng sự phủ định của giá trị đó.
b. Thêm cặp khóa / giá trị 'c': 40 vào dữ liệu.
c. Xóa giá trị tại khóa 'b' trong dữ liệu một cách an toàn.
d. In các phím trong dữ liệu theo thứ tự bảng chữ cái
Solution:
    The values of data={'b':20, 'a':35}
    a. data['b']=-20
    b. data['c']=40
    c. data.pop('b', 20)
    d.thekey=list(data)
    thekey.sort()
    for key in thekey:
        print(key)
    ....
"""