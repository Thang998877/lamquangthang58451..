"""
Author: Lâm Quang Thắng
Date: 24/10/2021
Program:
  Giai thừa của một số nguyên dương n, fact (n), được định nghĩa một cách đệ quy như sau:
     fact () n 1 5, khi n 1 5
     fact () n n 5 2 * fact n () 1, ngược lại
     Định nghĩa một thực tế hàm đệ quy trả về giai thừa của một số dương đã cho
     số nguyên.
Solution:

    ....
"""
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
