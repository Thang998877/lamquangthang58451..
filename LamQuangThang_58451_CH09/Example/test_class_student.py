from exampe_student import Student


if __name__ == '__main__':

    print(help(Student))

    student_a = Student("Lam Quang Thang",5)
    print("Ten: ", student_a.getName())
    print("diem: ", student_a.getScores())
    print("diem cua ban: ",student_a.getScore(2))

    student_a.setScore(1, 9.0)
    print("diem cua ban: ", student_a.getScore(1))
    print("======"*10)
    print(student_a)
