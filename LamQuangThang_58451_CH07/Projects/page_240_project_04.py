"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
Chương trình này hiển thị một bức tranh giống Mondrian với
mức đầu vào của người dùng.
Giải pháp:
    ....
"""

import random
from turtle import Turtle
from time import sleep

def fillRectangle(t, x1, y1, x2, y2):
    """Điền vào một hình chữ nhật với các điểm góc đã cho
     sử dụng một màu ngẫu nhiên."""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.pencolor(red, green, blue)
    t.fillcolor(red, green, blue)
    t.begin_fill()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()


def mondrian(t, x1, y1, x2, y2, level):
    """Vẽ một bức tranh giống Mondrian ở cấp độ đã cho."""
    if level > 0:
        fillRectangle(t, x1, y1, x2, y2)

        vertical = random.randint(1, 2)

        if vertical == 1:  # Chia dọc
            mondrian(t, x1, y1, (x2 - x1) / 3 + x1, y2,
                     level - 1)
            mondrian(t, (x2 - x1) / 3 + x1, y1, x2, y2,
                     level - 1)

        else:  # Chia ngang

            mondrian(t, x1, y1, x2, (y2 - y1) / 3 + y1,
                     level - 1)
            mondrian(t, x1, (y2 - y1) / 3 + y1, x2, y2,
                     level - 1)


def main():
    level = int(input("Nhập cấp độ: "))
    t = Turtle()
    t.hideturtle()
    width = t.screen.window_width() // 2
    height = t.screen.window_height() // 2
    mondrian(t, -width, height,
             width, -height, level)
    sleep(5)

main()
