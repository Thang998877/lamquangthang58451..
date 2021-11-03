"""
Author: Lâm Quang Thắng
Date: 10/10/2021
Program: Tạo câu
Solution:
    1. yêu cầu
    Viết chương trình tạo câu.
    2. phân tích
    Câu trong bất kỳ ngôn ngữ nào cũng có cấu trúc được xác định bởi một ngữ pháp. Chúng cũng bao gồm
    một tập hợp các từ từ từ vựng của ngôn ngữ. Từ vựng của một ngôn ngữ
    như tiếng Anh bao gồm hàng nghìn từ và các quy tắc ngữ pháp khá
    phức tạp. Vì mục đích đơn giản, chương trình của chúng tôi sẽ tạo ra các câu từ một tập hợp con đơn giản của tiếng Anh.
    Từ vựng sẽ bao gồm các từ mẫu từ một số
    các phần của bài phát biểu, bao gồm danh từ, động từ, mạo từ và giới từ. Từ những từ này,
    bạn có thể xây dựng các cụm danh từ, cụm giới từ và cụm động từ. Từ đó
    các cụm từ cấu thành, bạn có thể xây dựng câu. Ví dụ, câu “Cô gái đánh
    the ball with the bat ”chứa ba cụm danh từ, một cụm động từ và một cụm giới từ. Bảng 5-3 tóm tắt các quy tắc ngữ
    pháp cho tập hợp con tiếng Anh của chúng tôi.
    Quy tắc cho cụm danh từ nói rằng nó là một Điều sau đó là (1) một Danh từ. Do đó, một
    cụm danh từ có thể là "con dơi." Lưu ý rằng một số cụm từ trong cột bên trái của
    Bảng 5-3 cũng xuất hiện ở cột bên phải như các thành phần của các cụm từ khác. Mặc dù
    ngữ pháp này đơn giản hơn nhiều so với bộ quy tắc hoàn chỉnh cho ngữ pháp tiếng Anh,
    bạn vẫn có thể tạo ra các câu có cấu trúc khá hoàn chỉnh.
    Chương trình sẽ nhắc người dùng về số lượng câu cần tạo. Giao diện người dùng tư thế chuyên nghiệp như sau:
   Nhập số câu: 3
    THE BOY HIT THE BAT WITH A BOY
    THE BOY HIT THE BALL BY A BAT
    THE BOY SAW THE GIRL WITH THE GIRL
  Nhập số câu: 2
    A BALL HIT A GIRL WITH THE BAT
    A GIRL SAW THE BAT BY A BOY
   3. thiết kế
    Trong số nhiều cách để giải quyết vấn đề trong nghiên cứu điển hình này, có lẽ cách đơn giản nhất là
    để gán nhiệm vụ tạo từng cụm từ cho một chức năng riêng biệt. Mỗi chức năng
    xây dựng và trả về một chuỗi đại diện cho cụm từ của nó. Chuỗi này chứa các từ
    rút ra từ các phần của bài phát biểu và từ các cụm từ khác. Khi một chức năng cần một
    từ riêng lẻ, nó được chọn ngẫu nhiên từ các từ trong phần đó của bài phát biểu. Khi nào
    một hàm cần một cụm từ khác, nó gọi một hàm khác để xây dựng cụm từ đó. Các
    kết quả, tất cả các chuỗi, được nối với dấu cách và được trả về.
    Chức năng cho Câu là dễ nhất. Nó chỉ gọi các hàm cho cụm danh từ
    và Cụm động từ và nối các kết quả, như sau:
    câu def ():
        'Tạo và trả về một câu.'
        trả về danh từPhrase () + "" + verbPhrase () + "."
    Chức năng cho cụm danh từ chọn ngẫu nhiên một mạo từ và một danh từ từ từ vựng,
    nối chúng và trả về kết quả. Chúng tôi giả định rằng các bài báo về biến và
    danh từ chỉ bộ sưu tập các phần này của bài phát biểu và phát triển chúng sau này trong thiết kế.
    Hàm random.choice trả về một phần tử ngẫu nhiên từ một tập hợp như vậy.
    định nghĩa danh từPhrase ():
        'Tạo và trả về một cụm danh từ.'
        trả về random.choice (các bài báo) + "" + random.choice (danh từ)
    Thiết kế của hai chức năng cấu trúc cụm từ còn lại là tương tự.
    Chức năng chính điều khiển chương trình bằng một vòng điều khiển đếm:
    def main():
        'Allows the user to input the number of sentences to generate.'
        number = int(input("Enter the number of sentences: "))
        for count in range(number):
            print(sentence())
    Các mạo từ và danh từ biến được sử dụng trong các hàm của chương trình đề cập đến tập hợp các từ thực tế thuộc hai phần này của lời nói. Hai bộ sưu tập khác,
    động từ và giới từ được đặt tên, cũng sẽ được sử dụng. Cấu trúc dữ liệu được sử dụng để đại diện cho một tập hợp các từ sẽ cho phép chương trình chọn ngẫu nhiên một từ.
    Vì cấu trúc dữ liệu không thay đổi trong quá trình diễn ra chương trình, bạn
    có thể sử dụng nhiều chuỗi. Bốn bộ giá trị đóng vai trò như một nhóm dữ liệu chung cho các hàm func trong chương trình và được khởi tạo trước khi các hàm được xác định.
    4. thực hiện (Mã hóa)
    Khi các hàm sử dụng một nhóm dữ liệu chung, bạn nên xác định hoặc khởi tạo dữ liệu
    trước khi các chức năng được xác định. Do đó, các biến cho dữ liệu được khởi tạo chỉ
    bên dưới câu lệnh nhập.
    5. kiểm tra
    Thơ thì không, nhưng thử nghiệm vẫn quan trọng. Các chức năng được phát triển trong trường hợp này
    nghiên cứu có thể được kiểm tra theo cách từ dưới lên. Để làm như vậy, bạn phải khởi tạo dữ liệu
    đầu tiên. Sau đó, bạn có thể chạy ngay hàm cấp thấp nhất, nounPhrase để kiểm tra
    kết quả của nó và bạn có thể làm việc với các câu từ đó.
    Mặt khác, thử nghiệm cũng có thể tuân theo thiết kế, theo đường dẫn từ trên xuống.
    Bạn có thể bắt đầu bằng cách viết tiêu đề cho tất cả các hàm và các câu lệnh trả về đơn giản trả về tên của các hàm. Sau đó, bạn có thể hoàn thành mã cho chức năng sen tence trước, kiểm tra nó và tiếp tục đi xuống từ đó. Lập trình viên khôn ngoan
    cũng có thể kết hợp kiểm tra từ dưới lên và từ trên xuống nếu cần.
    ....
"""
import random
# Vocabulary: words in 4 different parts of speech
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
def sentence():
    """Builds and returns a sentence."""
    return nounphrase() + " " + verbphrase()
def nounphrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)
def verbphrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounphrase() + " " + \
    prepositionalphrase()
def prepositionalphrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounphrase()
def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
# The entry point for program execution
    if __name__ == "__main__":
        main()