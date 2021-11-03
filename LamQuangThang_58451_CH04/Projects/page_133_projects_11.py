"""
Author: Lâm Quang Thắng
Date: 26/09/2021
Program:
  Jack vừa hoàn thành chương trình phân tích văn bản Flesch từ chương này
nghiên cứu tình huống. Người giám sát của anh ấy, Jill, đã phát hiện ra một lỗi trong mã của anh ấy. Lỗi
khiến chương trình đếm một âm tiết có chứa các nguyên âm liên tiếp là nhiều
âm tiết. Đề xuất giải pháp cho vấn đề này trong mã của Jack và sửa đổi pro gram để nó xử lý các trường hợp này một cách chính xác.

Solution:

    ....
"""


# Lấy đầu vào.
fileName = input("Nhập tên tệp: ")
inputFile = open(fileName, 'r')
text = inputFile.read()
# Đếm số câu
cau = text.count('.') + text.count('?') + \
      text.count(':') + text.count(';') + \
      text.count('!')
# Đếm các từ
words = len(text.split())
# Đếm các âm tiết
am_tiet = 0
nguyen_am = 'aeiouAEIOU'
for words in text.split():
    for nguyen_am in nguyen_am:
        am_tiet += words.count(nguyen_am)
    for ending in ['es', 'ed', 'e']:
        if words.endswith(ending):
            am_tiet -= 1
    if words.endswith('le'):
        am_tiet += 1
# Tính chỉ số Thịt và cấp lớp
index = 206.835 - 1.015 * (words / cau) - \
       84.6 * (am_tiet / words)
level = int(round(0.39 * (words / cau) + 11.8 *\
                  (am_tiet / words) - 15.59))
# Xuất kết quả
print("Chỉ mục Flesch là", index)
print("Tương đương Cấp độ là", level)
print(words, "câu")
print(words, "từ")
print(am_tiet, "âm tiết")

