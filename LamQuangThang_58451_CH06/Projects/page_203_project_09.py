"""
Tác giả: Lâm Quang Thắng
Ngày: 23/10/2021
Vấn đề:
  Viết chương trình tính toán và in giá trị trung bình của các số trong một văn bản
tập tin. Bạn nên sử dụng hai hàm bậc cao hơn để đơn giản hóa thiết kế.

Giải pháp:
    ....
"""
from functools import reduce

filename = input("Nhap tep vao day: ")
inputfile=open(filename, 'r')

lyst = []
for line in inputfile:
    lyst.extend(line.split())
lyst = list(map(float, lyst))
sum = reduce(lambda x,y: x+y, lyst)
if len(lyst) == 0:
    average = 0
else:
    average = sum/len(lyst)
print("So trung binh la: ", average)