import turtle as tu
import random

def draw_ten_dots():
    for _ in range(10):
        color = random.choice(rgb_colors)
        tim.dot (dot_size,color)
        tim.penup()
        tim.forward(50)


tu.colormode(255)
rgb_colors= [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


tim=tu.Turtle()
tim.speed("fastest")
screen=tu.Screen()
dot_size=20
x_cord=-250
y_cord=-200

for _ in range(10):
    tim.penup()
    tim.setposition(x_cord,y_cord)
    draw_ten_dots()
    y_cord+=40
tim.hideturtle()
screen.exitonclick()