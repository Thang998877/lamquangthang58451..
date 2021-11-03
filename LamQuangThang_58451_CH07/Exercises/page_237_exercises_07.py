"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
  Tại sao chức năng làm mờ cần hoạt động với bản sao của ảnh gốc?
Giải pháp:
 Chức năng làm mờ mong đợi một hình ảnh như một đối số và
     trả về một bản sao của hình ảnh đó bị mờ. Chức năng làm mờ bắt đầu di chuyển ngang qua lưới
     với vị trí (1, 1) và kết thúc bằng vị trí (chiều rộng 2 2, chiều cao 2 2).
     Điều này có nghĩa là thuật toán không biến đổi các pixel trên các cạnh bên ngoài của hình ảnh
    ....
"""