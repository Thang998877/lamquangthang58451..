"""
Author: Lâm Quang Thắng
Date: 18/10/2021
Program: Recursive Patterns in Fractals
Solution:
    1. Request
    Write a program that allows the user to draw a particular c-curve at varying levels
    2. Analysis
    The proposed interface is shown in Figure 7-7. The program should prompt the user
    for the level of the c-curve. After this integer is entered, the program should display a
    Turtle graphics window in which it draws the c-curve.
    3. Design
    An N-level c-curve can be drawn with a recursive function. The function receives a
    Turtle object, the end points of a line segment, and the current level as arguments.
    At level 0, the function draws a simple line segment. Otherwise, a level N c-curve
    consists of two level N 2 1 c-curves, constructed as follows:
    Let xm be ( 1x x 1 12 1y y 2 2) // 2.
    Let ym be ( 2x y 1 11 2y x 2 1) // 2.
    The first level N 2 1 c-curve uses the line segment (x1, y1), (xm, ym), and level N 2 1,
    so the function is called recursively with these arguments.
    The second level N 2 1 c-curve uses the line segment (xm, ym), (x2, y2), and level
    N 2 1, so the function is called recursively with these arguments.
    For example, in a level-0 c-curve, let (x1, y1) be (50, –50) and (x2, y2) be (50, 50).
    Then, to obtain a level-1 c-curve, use the formulas for computing xm and ym to
    obtain (xm, ym), which is (0, 0). Figure 7-8 shows a solid line segment for the level-0
    c-curve and two dashed line segments for the level-1 c-curve that result from these
    operations. In effect, the operations produce two shorter line segments that meet at
    right angles.
    Here is the pseudocode for the recursive algorithm:
    function cCurve(t, x1, y1, x2, y2, level)
     if level == 0:
     drawLine(x1, y1, x2, y2)
     else
     xm = (x1 + x2 + y1 - y2) // 2
     ym = (x2 + y1 + y2 - x1) // 2
     cCurve(t, x1, y1, xm, ym, level - 1)
     cCurve(t, xm, ym, x2, y2, level - 1)
    The function drawLine uses the turtle to draw a line between two given endpoints.
    4.Implementation (Coding)
    The program includes the three function definitions of cCurve, drawLine, and main.
    Because drawLine is an auxiliary function, its definition is nested within the definition
    of cCurve. In addition to the Turtle class, the program imports the functions tracer
    and update from the turtle module. Because c-curves with large degrees can take
    a long time to draw, you can suspend the turtle’s output until the entire shape has
    been internally generated.
    ....
"""

from turtle import Turtle, tracer, update
def ccurve(t, x1, y1, x2, y2, level):
    def drawline(x1, y1, x2, y2):
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)
    if level == 0:
        drawline(x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        ccurve(t, x1, y1, xm, ym, level - 1)
        ccurve(t, xm, ym, x2, y2, level - 1)
def main():
    level = int(input("Nhập cấp độ (0 trở lên): "))
    t = Turtle()
    if level > 8:
        tracer(False)
    t.pencolor("blue")
    t.hideturtle()
    ccurve(t, 50, -50, 50, 50, level)
    if level > 8:
        update()
if __name__ == "__main__":
    main()