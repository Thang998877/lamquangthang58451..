"""
Author: Lâm Quang Thắng
Date: 10/10/2021
Program: Liệu pháp tâm lý không hoạt động
Solution:
   1. yêu cầu
     Viết một chương trình mô phỏng một nhà trị liệu tâm lý không hoạt động.
     2. phân tích
     Phân tích
     Hình 5-4 cho thấy giao diện của chương trình khi nó thay đổi trong một chuỗi
     trao đổi với người dùng.
     Khi người dùng nhập một câu lệnh, chương trình sẽ phản hồi theo một trong hai cách:
     1. Với hàng rào được chọn ngẫu nhiên, chẳng hạn như "Vui lòng cho tôi biết thêm."
     2. Bằng cách thay đổi một số từ khóa trong chuỗi đầu vào của người dùng và nối chuỗi này
     đến một vòng loại được chọn ngẫu nhiên. Do đó, để "Giáo viên của tôi luôn chơi các video yêu thích",
     chương trình có thể trả lời, "Tại sao bạn nói rằng giáo viên của bạn luôn chơi các trò chơi yêu thích?"
     Hình 5-4 Một phiên với chương trình bác sĩ
     'Chào buổi sáng, tôi hy vọng hôm nay bạn khỏe.
    What can I do for you?
    >> My mother and I don't get along
    Why do you say that your mother and you don't get along
    >> she always favors my sister
    You seem to think that she always favors your sister
    >> my dad and I get along fine
    Can you explain why your dad and you get along fine
    >> he helps me with my homework
    Please tell me more
    >> quit
    Have a nice day!'
   Khi người dùng nhập một câu lệnh, chương trình sẽ phản hồi ở một trong 3
    Chương trình bao gồm một tập hợp các chức năng cộng tác chia sẻ một dữ liệu chung
    Hồ bơi.
    Hai trong số các tập dữ liệu là hàng rào và vòng loại. Bởi vì những bộ sưu tập này làm
    không thay đổi và các phần tử của chúng phải được chọn ngẫu nhiên, bạn có thể sử dụng các bộ giá trị để
    đại diện cho họ. Tên của họ, tất nhiên, là hàng rào và vòng loại.
    Tập dữ liệu khác bao gồm các ánh xạ giữa các đại từ ngôi thứ nhất và
    đại từ ngôi thứ hai. Ví dụ: khi chương trình nhìn thấy “tôi” trong một bệnh nhân
    đầu vào, nó sẽ trả lời bằng một câu có chứa “bạn”. Loại dữ liệu tốt nhất
    cấu trúc để giữ các mối tương quan này là một từ điển. Từ điển này có tên
    vật thay thế.
    Chức năng chính hiển thị lời chào, hiển thị lời nhắc và chờ người dùng nhập.
    Sau đây là mã giả cho vòng lặp chính:
    gửi lời chào đến bệnh nhân
    trong khi Đúng
        prompt for and input a string from the patient
        if the string equals "Quit"
            output a sign-off message to the patient
            break
        call another function to obtain a reply to this string
        output the reply to the patient
    Nhà trị liệu của chúng tôi có thể không phải là một chuyên gia, nhưng không phải trả phí cho các dịch vụ của họ. Là gì
     hơn nữa, bác sĩ trị liệu của chúng tôi dường như sẵn sàng tiếp tục điều trị mãi mãi. Tuy nhiên, nếu bệnh nhân phải bỏ
     để làm điều gì đó khác, cô ấy có thể làm như vậy bằng cách gõ "thoát" để kết thúc chương trình.
     Hàm trả lời mong đợi chuỗi của bệnh nhân như một đối số và trả về chuỗi khác
     chuỗi như câu trả lời. Chức năng này thực hiện hai chiến lược để thực hiện trả lời
     được đề xuất trong giai đoạn phân tích. Một phần tư thời gian bảo hành hàng rào.
     Nếu không, chức năng sẽ xây dựng câu trả lời của nó bằng cách thay đổi những người trong bệnh nhân
     nhập và nối kết quả vào một vòng loại được chọn ngẫu nhiên. Chức năng trả lời
     gọi thêm một hàm khác, changePerson, để thực hiện nhiệm vụ phức tạp là thay đổi
     người
    def reply(sentence):
        'Builds and returns a reply to the sentence.'
        probability = random.randint(1, 4)
        if probability == 1:
            return random.choice(hedges)
        else:
            trả về random.choice (vòng loại) + changePerson (câu)
     Hàm changePerson trích xuất danh sách các từ từ chuỗi của bệnh nhân. Sau đó nó
     xây dựng một danh sách mới trong đó bất kỳ khóa đại từ nào trong từ điển thay thế đều được thay thế
     bởi đại từ / giá trị của nó. Danh sách này sau đó được chuyển đổi trở lại thành một chuỗi và được trả về.
     161
    def changePerson(sentence):
        'Replaces first person pronouns with second person
        pronouns.'
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(replacements.get(word, word))
        return " ".join(replyWords)
    Lưu ý rằng nỗ lực để lấy một thay thế từ từ điển thay thế
    hoặc thành công và trả về một đại từ thay thế thực sự, hoặc nỗ lực không thành công và
    trả về từ ban đầu. Phương thức nối chuỗi liên kết các từ với nhau từ
    danh sách trả lời của AdWords với một ký tự khoảng trắng làm dấu phân cách.
    4. thực hiện (Mã hóa)
    Cấu trúc của chương trình này giống với cấu trúc của trình tạo câu được phát triển trong
    nghiên cứu trường hợp đầu tiên của chương này. Ba cấu trúc dữ liệu được khởi tạo gần
    đầu chương trình, và chúng không bao giờ thay đổi. Ba chức năng hợp tác trong
    một cách thẳng thắn
    5. kiểm tra
    Như trong chương trình tạo câu, các chức năng trong chương trình này có thể được kiểm tra trong
    theo cách từ dưới lên hoặc từ trên xuống. Như bạn sẽ thấy, các câu trả lời của chương trình được chia nhỏ
    khi người dùng nói với nhà trị liệu ở ngôi thứ hai, khi người dùng nhập
    co thắt (ví dụ: tôi và tôi sẽ), khi người dùng liên hệ trực tiếp với bác sĩ
    với những câu như “Bạn không nghe tôi nói” và theo nhiều cách khác. Như bạn sẽ
    xem trong Dự án ở cuối chương này, với một chút công việc bạn có thể thực hiện
    trả lời thực tế hơn.

"""
import random
hedges = ("Please tell me more.",
        "Many of my patients tell me the same thing.",
        "Please continue.")
qualifiers = ("Why do you say that ",
            "You seem to think that ",
            "Can you explain why ")
replacements = {"I":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours"}
def reply(sentence):
    """Builds and returns a reply to the sentence."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changeperson(sentence)
def changeperson(sentence):
    """Replaces first person pronouns with second person
    pronouns."""
    words = sentence.split()
    replywords = []
    for word in words:
        replywords.append(replacements.get(word, word))
        return " ".join(replywords)
def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))
# The entry point for program execution
if __name__ == "__main:":
    main()