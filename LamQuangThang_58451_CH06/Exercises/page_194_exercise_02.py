"""
Author: Lâm Quang Thắng
Date: 24/10/2021
Program:
  Phạm vi của một biến là gì? Cho một ví dụ.
Solution:
  - Trong văn bản thông thường, ý nghĩa của một từ thường phụ thuộc vào ngữ cảnh xung quanh của nó. Vì
     ví dụ, trong mục thể thao của tờ báo, từ "bat" có nghĩa là một cây gậy để đánh
     bóng chày, trong khi trong một câu chuyện về ma cà rồng, nó có nghĩa là một loài động vật có vú biết bay. Trong một chương trình,
     ngữ cảnh cung cấp cho một cái tên một ý nghĩa được gọi là phạm vi của nó
     - Một ví dụ:
     x = 5
     def f ():
         x = 10 # Cố gắng đặt lại x
     f () # X cấp cao nhất có thay đổi không?
     print (x) # Không, điều này hiển thị 5
     Khi hàm f được gọi, nó không gán 10 cho biến môđun x; thay vào đó, nó chỉ định
     10 thành một biến tạm thời x. Trên thực tế, khi biến tạm thời được giới thiệu, mô-đun
     biến không còn hiển thị trong hàm f. Trong mọi trường hợp, giá trị của biến mô-đun vẫn
     không thay đổi bởi cuộc gọi. Có một cách để cho phép một hàm sửa đổi một biến mô-đun, nhưng trong
     Chương 9 chúng ta khám phá một cách tốt hơn để quản lý các nhóm dữ liệu phổ biến yêu cầu thay đổi.
    ....
"""