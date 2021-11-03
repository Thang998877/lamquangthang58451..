"""
Author: Lâm Quang Thắng
Date: 10/10/2021
Program: Phương pháp đột biến là gì? Giải thích tại sao các phương thức đột biến thường trả về
giá trị Không có.
Solution:
   - Các đối tượng có thể thay đổi (chẳng hạn như danh sách) có một số phương thức dành riêng
     hoàn toàn để sửa đổi trạng thái bên trong của đối tượng.
     - Bởi vì sự thay đổi trạng thái là tất cả những gì mong muốn, một phương thức mutator thường không trả về giá trị quan tâm nào cho người gọi (nhưng lưu ý rằng
     pop là một ngoại lệ đối với quy tắc này) Tuy nhiên, Python tự động trả về giá trị đặc biệt Không có
     ngay cả khi một phương thức không trả về một giá trị rõ ràng. Chúng tôi đề cập đến điều này bây giờ chỉ như một cảnh báo
     chống lại loại lỗi sau
    ....
"""