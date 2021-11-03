"""
Author: Lâm Quang Thắng
Date: 24/10/2021
Program:
  Thời gian tồn tại của một biến là gì? Cho một ví dụ.
Solution:
  - Một chương trình máy tính có hai bản chất. Một mặt, chương trình là một đoạn văn bản chứa những cái
  tên mà con người có thể đọc để hiểu một ý nghĩa nào đó. Nhìn từ góc độ này,
     các biến trong chương trình có phạm vi xác định khả năng hiển thị của chúng. Mặt khác, một
     chương trình mô tả một quá trình tồn tại trong một khoảng thời gian trên máy tính thực. Đã xem
     từ góc độ khác này, các biến của chương trình có một thuộc tính quan trọng khác được gọi là
     cả đời.
     - Một ví dụ:
     Khái niệm thời gian tồn tại giải thích sự tồn tại của hai biến được gọi là x trong
     phiên ví dụ. Biến mô-đun x tồn tại trước biến tạm thời x và tồn tại sau lệnh gọi của hàm f.
     Trong quá trình gọi f, bộ nhớ tồn tại cho cả hai
     các biến, vì vậy giá trị của chúng vẫn khác biệt. Một cơ chế tương tự để quản lý việc lưu trữ liên quan
     đến các tham số của lời gọi hàm đệ quy đã được thảo luận trong phần trước.
    ....
"""