"""
Author: Lâm Quang Thắng
Date: 17/09/2021
Program:
   Sửa đổi chương trình trò chơi đoán của Phần 3.5 để người dùng nghĩ về
 số mà máy tính phải đoán. Máy tính không được nhiều hơn
 số lần đoán tối thiểu và nó phải ngăn người dùng gian lận bằng cách
 nhập gợi ý gây hiểu lầm. (Gợi ý: Sử dụng hàm math.log để tính toán số lượng phỏng đoán tối thiểu cần thiết sau khi nhập giới hạn dưới và giới hạn trên
Solution:
    ....
"""
import math
import random

print('Chào mừng bạn đến với trò chơi đoán số')
print('Hãy đoán một số từ 0 - 100:')
# Tạo một số ngẫu nhiên từ 0 đến 100.
rand_num = random.randint(0, 100)
max_guesses = round(math.log(100 - 0 + 1, 2))
print("Bạn có", max_guesses, "cơ hội để đoán số!\n")
# Tạo một biến để đếm số lần đoán.
count = 0

while True:
    # Số lượng tăng dần
    count = count + 1

    # Kiểm tra xem số lượt có nhiều hơn số lượt đã cho hay không
    if count > max_guesses:
        print("Bạn đã vượt quá số lần đoán.")
        print("Con số là",rand_num)
        break;
    player_guess = int(input('Hãy đoán một số từ 0 - 100:'))
    if player_guess == rand_num:
        print("Bạn đoán số trong", count, "lần lượt !")
        break;
    elif player_guess < rand_num:
        print("Con số cao hơn")
    elif player_guess > rand_num:
        print("Con số thấp hơn")