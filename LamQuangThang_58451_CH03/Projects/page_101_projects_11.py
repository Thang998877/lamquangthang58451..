"""
Author: Lâm Quang Thắng
Date: 18/09/2021
Program:
   Trong trò chơi Lucky Sevens, người chơi tung một cặp xúc xắc. Nếu các dấu chấm cộng lại lên đến 7,
người chơi thắng $ 4; nếu không, người chơi mất $ 1. Giả sử rằng, để lôi kéo mòng biển,
 sòng bạc nói với người chơi rằng có rất nhiều cách để giành chiến thắng: (1, 6), (2, 5), v.v.
trên. Một phân tích toán học nhỏ cho thấy rằng không có đủ cách để giành chiến thắng
để làm cho trò chơi trở nên đáng giá; tuy nhiên, vì nhiều người nhìn chằm chằm vào
ở lần đầu tiên đề cập đến toán học, thách thức của bạn là viết một chương trình
thể hiện sự vô ích của việc chơi trò chơi. Chương trình của bạn sẽ được coi là đầu vào
số tiền mà người chơi muốn đặt vào nồi và chơi trò chơi
cho đến khi hết nồi. Tại thời điểm đó, chương trình sẽ in ra số
cuộn nó cần để phá vỡ người chơi, cũng như số tiền tối đa trong nồi.

Solution:
    ....
"""
import random

def playRound(budget: int) -> tuple:

    sum = sumOfDice(random.randint(1,6), random.randint(1,6))
    if sum == 7:
        budget += 4
        return ("Thắng",budget)
    else:
        budget -= 1
        return ("Thua",budget)

def sumOfDice(die1: int, die2: int) -> int:
        return die1 + die2

def haveMoney(budget: int) -> bool:
    # Đây là một biểu thức bậc ba, nó là một câu lệnh if trong một dòng
    return True if budget > 0 else False

def main():
    numRolls = 0

    outputString = "\t{0}\t\t{1}\t\t{2}"

    # To prevent a type error, the string is explicitly converted to int
    budget = int(input("Ngân sách cờ bạc của bạn là bao nhiêu?"))

    # \t is the metacharacter representing a tab
    print("Số cuộn\t\tThắng hay thua\tGiá trị hiện tại của nồi")

    print(outputString.format(numRolls, "Đặt", budget))

    # Giá trị trả về là kiểu boolean, do đó đầu ra là biểu thức
    while haveMoney(budget):
        # Python không hỗ trợ toán tử tăng trước hoặc tăng sau
        numRolls += 1
        output = playRound(budget)
        budget = output[1]
        print(outputString.format(numRolls, output[0], output[1]))

    print("Xin lỗi bạn hết tiền")

# Điểm đầu vào cho một chương trình Python
if __name__ == "__main__":
    main()
    # Giải pháp của bạn hoạt động nhưng nó không cần một chức năng chuyên dụng
    while True:
        userIn = input("Bạn có muốn chơi lại không?")
        if 'có' == userIn:
            main()
        else:
            print("tạm biệt")
            break