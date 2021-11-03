"""
Author: Lâm Quang Thắng
Date: 10/10/2021
Program: Giả sử rằng dữ liệu biến tham chiếu đến danh sách [5, 3, 7]. Viết các biểu thức
thực hiện các tác vụ sau:
   a. Thay thế giá trị ở vị trí 0 trong dữ liệu bằng phủ định của giá trị đó.
     b. Thêm giá trị 10 vào cuối dữ liệu.
     c. Chèn giá trị 22 ở vị trí 2 trong dữ liệu.
     d. Xóa giá trị ở vị trí 1 trong dữ liệu
     e. Thêm các giá trị trong danh sách newData vào cuối dữ liệu.
     f. Định vị chỉ mục của giá trị 7 trong dữ liệu, một cách an toàn.
     g. Sắp xếp các giá trị trong dữ liệu.
Solution:
    a.list = [5,3,7]
    list[0]=-5
    list
    b.list = [5,3,7]
    list[2]=10
    list
    c.list =[5,3,7]
    list[1]=22
    list
    d.list = [5,3,7]
    list.pop(0)
    list
    e.new_data=[1,2,3]
    new_data.append(6)
    new_data
    f. list = [5,3,7]
    target = 7
    if target in list:
        print(list.index(target))
    else:
        print(-l)
    f. list = [5,3,7]
    list.sort()
    list
    ....
"""