"""
Author: Lâm Quang Thắng
Date: 24/10/2021
Program:
  Ba phiên bản của hàm tổng kết đã được trình bày trong chương này.
Một sử dụng vòng lặp, một sử dụng đệ quy và một sử dụng hàm giảm. Thảo luận về
chi phí và lợi ích của mỗi phiên bản, về thời gian của lập trình viên và tính toán
tài nguyên cần thiết.
Solution:
  # Vòng:
    - Những lợi ích:
    + Bạn có thể thực hiện một câu lệnh nhiều lần bạn muốn
    - Trị giá:
    + Nó có thể lãng phí không gian trong chương trình của bạn
    # Đệ quy:
    - Những lợi ích:
    + Các giải pháp đệ quy thường tự nhiên và thanh lịch hơn các giải pháp lặp lại của chúng
    đối tác
    + Hàm đệ quy phát sinh khi người lập trình không xác định được trường hợp cơ sở hoặc để giảm
    quy mô của vấn đề theo cách kết thúc quá trình đệ quy
    - Các chi phí:
    + Hệ thống thời gian chạy trên máy tính thực, chẳng hạn như PVM, phải dành một số chi phí cho các lệnh gọi hàm đệ quy
    + Khi do lỗi thiết kế, đệ quy là vô hạn, ngăn xếp
    các khung được thêm vào cho đến khi PVM hết bộ nhớ, điều này sẽ tạm dừng chương trình với
    thông báo lỗi.
    + Ngược lại, vấn đề tương tự thường có thể được giải quyết bằng cách sử dụng một vòng lặp với số lượng không đổi
    bộ nhớ, dưới dạng hai hoặc ba biến. Bởi vì dung lượng bộ nhớ cần thiết cho
    vòng lặp không phát triển theo kích thước của tập dữ liệu của vấn đề, số lượng xử lý
    thời gian để quản lý bộ nhớ này cũng không tăng lên.
    + một số vấn đề với giải pháp lặp lại vẫn phải sử dụng
    cấu trúc dữ liệu giống như ngăn xếp rõ ràng, vì vậy giải pháp đệ quy có thể đơn giản hơn và không kém phần
    Có hiệu quả.
    # Giảm:
    ....
"""