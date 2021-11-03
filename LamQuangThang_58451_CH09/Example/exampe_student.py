"""
Tác giả: Lâm Quang Thắng
lop: CA20B1
Vấn đề
  Tài nguyên để quản lý tên và điểm thi của học sinh.
Giải pháp:

    ....
"""

from functools import reduce


class Student(object):
     """Đại diện cho một học sinh."""

     def __init__(self, name, number):
        """Hàm tạo tạo một Sinh viên với tên và số điểm và đặt tất cả các điểm đến 0."""
        self._name = name
        self._scores = []
        for count in range(number):
            self._scores.append(8)

     def getName(self):
         """Trả về tên của học sinh."""
         return self._name

     def getScores(self):
         """Trả về tên của học sinh."""
         return self._scores

     def setScore(self, i, score):
         """Đặt lại điểm thứ i, tính từ 1."""
         self._scores[i - 1] = score

     def getScore(self, i):
         """Trả về điểm thứ i, đếm từ 1."""
         return self._scores[i - 1]

     def getAverage(self):
         """Trả về điểm trung bình."""
         sum = reduce(lambda  x,y: x + y,self._scores)
         return sum / len(self._scores)

     def getHighScore(self):
         """Trả về điểm số cao nhất."""
         return max(self._scores)

     def __str__(self):
         """Trả về biểu diễn chuỗi của học sinh."""
         return "Name: " + self._name + "\nScores: " + \
                " ".join(map(str, self._scores))


if __name__ == '__main__':

    student_a = Student("Lam Quang Thang",5)
    print("Ten: ", student_a.getName())
    print("diem: ", student_a.getScores())
    print("diem cua ban: ",student_a.getScore(2))

    student_a.setScore(1, 9.0)
    print("diem cua ban: ", student_a.getScore(1))
    print("======"*10)
    print(student_a)

