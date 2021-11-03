"""
Author: Lâm Quang Thắng
Date: 09/10/2021
Program:
 Sự phù hợp tệp theo dõi các từ duy nhất trong tệp và tần số của chúng. Viết
một chương trình hiển thị sự phù hợp cho một tệp. Chương trình sẽ xuất ra
các từ duy nhất và tần số của chúng theo thứ tự bảng chữ cái. Các biến thể là để theo dõi
chuỗi của hai từ và tần số của chúng, hoặc n từ và tần số của chúng.

Solution:
    ....
"""
f = ("LAM QUANG THANG LAM QUANG THANG QUANG THANG LAM")
myDict = {}
linenum = 0
for word in f.split():
    if not word in myDict:
        myDict[word] = []
    myDict[word].append(linenum)
print("%-15s %-15s" % ("Word", "Frequency"))
for key in sorted(myDict):
    print('%-15s: %-15d' % (key, len(myDict[key])))
