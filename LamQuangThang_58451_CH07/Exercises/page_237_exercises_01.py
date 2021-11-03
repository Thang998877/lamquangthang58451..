"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
  Giải thích những ưu điểm và nhược điểm của các chương trình nén tệp hình ảnh không mất dữ liệu và mất dữ liệu.
Giải pháp:
  - Thuận lợi:
     + Hình ảnh được hiển thị, các giá trị màu gốc được khôi phục trong quá trình
     quá trình giải nén (Nén không mất dữ liệu)
     + Để tiết kiệm nhiều bit hơn nữa, một lược đồ khác sẽ phân tích các vùng pixel lớn hơn
     và lưu giá trị màu mà màu của pixel gần đúng (lược đồ Lossy)
     - Nhược điểm:
     + Một số thông tin màu gốc bị mất
     + Khi hình ảnh được giải nén và hiển thị, mắt người thường không thể phát hiện ra sự khác biệt
     giữa màu mới và màu ban đầu.
    ....
"""