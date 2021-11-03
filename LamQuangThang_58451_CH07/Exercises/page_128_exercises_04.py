"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
  Các hàm vẽ đa giác trong mô-đun đa giác có cùng một mẫu, khác nhau
chỉ ở số cạnh (số lần lặp của vòng lặp). Biến mô hình này thành một mô hình tổng quát hơn
hàm có tên polygon, lấy số lượng cạnh làm đối số bổ sung

Giải pháp:

    ....
"""
def pentagon(t, length):
    for count in range(5):
        t.forward(length)
        t.left(60)