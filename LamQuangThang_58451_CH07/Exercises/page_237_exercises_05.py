"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
  Đường truyền chính theo cột của lưới sẽ hoạt động như thế nào? Viết một đoạn mã
in các vị trí được truy cập bởi một đường ngang cột chính của lưới 2 x 3.

Giải pháp:
  - - Một cấu trúc vòng lặp lồng nhau được sử dụng để truy cập từng vị trí trong lưới hai chiều. Trong một
     truyền qua hàng-chính, vòng lặp bên ngoài của cấu trúc này di chuyển xuống các hàng bằng cách sử dụng
     tọa độ y và vòng lặp bên trong di chuyển qua các cột bằng cách sử dụng tọa độ x. Mỗi
     cột trong một hàng được truy cập trước khi chuyển sang hàng tiếp theo. Truyền tải chính theo cột
     đảo ngược các cài đặt này.
    ....
"""
width = 2
height = 3
for y in range(height):
    for x in range(width):
        print((x, y), end = " ")