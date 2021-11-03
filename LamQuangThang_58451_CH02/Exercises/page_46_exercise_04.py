"""
Author: Lâm Quang Thắng
Date: 06/09/2021
Problem: Điều gí xảy ra khi hàm in,in ra một chuỗi nghĩa đen với các kí tự dòng mới đc nhúng?
Solution:
    - Example: We write this string in the Python shell: 
    >>> print("""This very long sentence extends all the way to the next line.""")
    - It's will display this sentence: 
    "SyntaxError: invalid syntax
    >>> print("""This very long sentence extends... all the way to the next\n line."""")
    This very long sentence extends
    all the way to the next
    ....
"""
