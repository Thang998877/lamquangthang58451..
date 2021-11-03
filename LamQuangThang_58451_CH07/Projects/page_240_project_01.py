"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
 Vẽ một vòng tròn.
  1. Các đầu vào là tọa độ của điểm trung tâm và bán kính.
Giải pháp:
    ....
"""

import math
from turtle import Turtle
from time import sleep

def drawCircle(t, x, y, radius):
    """Vẽ một đường tròn với tâm và bán kính đã cho."""
    t.up()
    t.goto(x + radius, y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius / 120.0)


def main():
    """Cho phép người dùng nhập điểm trung tâm và bán kính."""
    x = int(input("Nhập tọa độ x của điểm chính giữa: "))
    y = int(input("Nhập tọa độ y của điểm trung tâm: "))
    radius = int(input("Nhập bán kính: "))
    drawCircle(Turtle(), x, y, radius)
    sleep(5)


if __name__ == '__main__':
    main()