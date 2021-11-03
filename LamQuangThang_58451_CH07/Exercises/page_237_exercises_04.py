"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
  Mô tả cách duyệt chính theo hàng truy cập vào mọi vị trí trong lưới hai chiều.
Giải pháp:
  - Cấu trúc vòng lặp lồng nhau được sử dụng để thăm từng vị trí trong lưới hai chiều. Trong một
     truyền qua hàng-chính, vòng lặp bên ngoài của cấu trúc này di chuyển xuống các hàng bằng cách sử dụng
     tọa độ y và vòng lặp bên trong di chuyển qua các cột bằng cách sử dụng tọa độ x. Mỗi
     cột trong một hàng được truy cập trước khi chuyển sang hàng tiếp theo. Truyền tải chính theo cột
     đảo ngược các cài đặt này.
    ....
"""