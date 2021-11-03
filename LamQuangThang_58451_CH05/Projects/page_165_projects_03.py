"""
Author: Lâm Quang Thắng
Date: 05/10/2021
Program:
  Sửa đổi chương trình tạo câu của Nghiên cứu điển hình 5.3 để nó đưa vào
từ vựng từ một tập hợp các tệp văn bản khi khởi động. Tên tệp là danh từ.txt, động từ.txt,
 bài viết.txt và giới từ.txt. (Gợi ý: Xác định một hàm mới,
get AdWords. Hàm này sẽ yêu cầu một tên tệp làm đối số. Chức năng
nên mở tệp đầu vào với tên này, xác định danh sách tạm thời, đọc các từ
từ tệp và thêm chúng vào danh sách. Sau đó, hàm sẽ chuyển đổi danh sách
vào một bộ giá trị và trả lại bộ giá trị này. Gọi hàm với một tên tệp thực tế để sắp xếp từng biến trong số bốn biến cho từ vựng.)

Solution:

    ....
"""


import random
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def sentence():
 return nounPhrase() + " " + verbPhrase()
def nounPhrase():
 return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
 return random.choice(verbs) + " " + nounPhrase() + " " + \
prepositionalPhrase()
def prepositionalPhrase():
  return random.choice(prepositions) + " " + nounPhrase()

def main():
    number= int(input("Nhập số câu: "))
    for count in range(number):
      print(sentence())

if __name__ == "__main__":
  main()
