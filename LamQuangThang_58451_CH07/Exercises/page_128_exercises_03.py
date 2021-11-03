"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
 Thêm một chức năng có tên vòng tròn vào mô-đun đa giác. Hàm này mong đợi
đối số tương tự như các hàm vuông và lục giác. Hàm sẽ vẽ một
khoanh tròn. (Gợi ý: vòng lặp lặp lại 360 lần.)

Giải pháp:

    ....
"""
def circle(t, length):
    for count in range(360):
        t.forward(length)
        t.left(90)