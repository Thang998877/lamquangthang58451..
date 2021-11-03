"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
 Chương trình này hiển thị một bông tuyết Koch bằng cách sử dụng
mức đầu vào của người dùng.

Vẽ các đoạn thẳng bằng màu sắc ngẫu nhiên.
Giải pháp:
    ....
"""

from time import sleep
from turtle import Turtle


def drawKochFractal(width, height, size, level):
    """Vẽ một fractal Koch có cấp độ và kích thước nhất định."""
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(-width // 3, height // 4)
    t.down()
    drawFractalLine(t, size, 0, level)
    drawFractalLine(t, size, -120, level)
    drawFractalLine(t, size, 120, level)


def drawFractalLine(t, distance, theta, level):
    """Vẽ một đường đơn theo một hướng nhất định
     hoặc bốn đường fractal theo hướng mới."""
    if (level == 0):
        drawPolarLine(t, distance, theta)
    else:
        drawFractalLine(t, distance // 3, theta, level - 1)
        drawFractalLine(t, distance // 3, theta + 60, level - 1)
        drawFractalLine(t, distance // 3, theta - 60, level - 1)
        drawFractalLine(t, distance // 3, theta, level - 1)


def drawPolarLine(t, distance, theta):
    """Di chuyển khoảng cách đã cho theo hướng nhất định."""
    t.setheading(theta)
    t.forward(distance)


if __name__ == '__main__':
    level = int(input("Nhập cấp độ: "))
    drawKochFractal(200, 200, 150, level)
    sleep(5)