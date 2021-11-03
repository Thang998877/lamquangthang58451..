"""
Author: Lâm Quang Thắng
Date: 24/10/2021
Program:
  Viết mã giảm tạo một chuỗi đơn từ danh sách các chuỗi có tên
từ
Solution:

    ....
"""
words = ['alfa', 'bravo', 'charlie', 'delta', 'gamma', 'lambda']
from functools import reduce
print(reduce(lambda x,y:x+y,map(lambda x:x[0],words)))