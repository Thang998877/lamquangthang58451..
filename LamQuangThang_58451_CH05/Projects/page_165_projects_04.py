"""
Author: Lâm Quang Thắng
Date: 09/10/2021
Program:
 Thực hiện các sửa đổi sau đối với chương trình tạo câu gốc:
a. Cụm giới từ là tùy chọn. (Nó có thể xuất hiện với một số
xác suất.)
b. Một mệnh đề kết hợp và một mệnh đề độc lập thứ hai là tùy chọn: Cậu bé đã lấy một
uống rượu và cô gái chơi bóng chày.
c. Một tính từ là tùy chọn: Cô gái đá quả bóng màu đỏ bị đau chân.
Bạn nên thêm các biến mới cho các tập hợp tính từ và liên từ.

Solution:

    ....
"""
import random
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL",)
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
def sentence():
# Tạo và trả về một câu.
     return nounPhrase() + " " + verbPhrase()
def nounPhrase():
# Tạo và trả về một cụm danh từ.
    return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
# Tạo và trả về một cụm động từ.
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()
def prepositionalPhrase():
# Tạo và trả về một cụm giới từ.
    return random.choice(prepositions)+ " " + nounPhrase()
def main():
# Cho phép người dùng nhập số lượng câu để tạo.
     number = int(input("Nhập số câu: "))
     for count in range(0, number):
        print(sentence())
main()
