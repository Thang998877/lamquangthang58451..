"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
 Chương trình này nhắc người dùng về mức
một đường cong c và vẽ một đường cong c của mức đó.

Vẽ các đoạn thẳng bằng màu sắc ngẫu nhiên.
Giải pháp:
    ....
"""

import random
from time import sleep
from turtle import Turtle


def cCurve(t, x1, y1, x2, y2, level):
    def drawLine(x1, y1, x2, y2):
        """Vẽ một đoạn thẳng giữa các điểm cuối,
         sử dụng một màu ngẫu nhiên."""
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)

    if level == 0:
        drawLine(x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        cCurve(t, x1, y1, xm, ym, level - 1)
        cCurve(t, xm, ym, x2, y2, level - 1)


def main():
    level = int(input("Nhập cấp độ (0 trở lên): "))
    t = Turtle()
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    t.pencolor(r, g, b)
    t.hideturtle()
    cCurve(t, 50, -5, 50, 50, level)
    sleep(5)


if __name__ == '__main__':
    main()