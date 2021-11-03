"""
Author: Lâm Quang Thắng
Date: 25/09/2021
Program:
 Viết một đoạn mã in tên của tất cả các mục trong hiện tại
thư mục làm việc.

Solution:

    ....
"""
import os
for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)
