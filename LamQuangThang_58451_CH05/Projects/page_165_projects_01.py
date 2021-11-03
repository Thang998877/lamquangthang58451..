"""
Author: Lâm Quang Thắng
Date: 05/10/2021
Program:
   Một nhóm các nhà thống kê tại một trường cao đẳng địa phương đã yêu cầu bạn tạo một tập hợp các hàm
tính toán giá trị trung bình và chế độ của một tập hợp số, như được định nghĩa trong Phần
5.4. Xác định các chức năng này trong một mô-đun có tên là stats.py. Cũng bao gồm một chức năng
có tên là mean, tính giá trị trung bình của một tập hợp các số. Mỗi chức năng
nên mong đợi một danh sách các số dưới dạng đối số và trả về một số duy nhất. Mỗi
hàm sẽ trả về 0 nếu danh sách trống. Bao gồm một chức năng chính kiểm tra
ba hàm thống kê với một danh sách nhất định.

Solution:

    ....
"""

def median(numbers):
    numbers.sort()
    midIndex = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midIndex]
    else:
        return (numbers[midIndex] + numbers[midIndex - 1]) / 2
def mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)
def mode(numbers):
    result = numbers[0]
    count = 0
    for num in numbers:
        if numbers.count(num) >= count:
            count = numbers.count(num)
            result = num
    return result
def main():
    userList = [3, 1, 7, 1, 4, 10]
    print("danh sách:", userList)
    print("chế độ:", mode(userList))
    print("trung bình:", median(userList))
    print("Mean:", mean(userList))
main()