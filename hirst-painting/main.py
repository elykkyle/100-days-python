import colorgram
from random import choice
from turtle import Turtle, Screen

t = Turtle()
t.speed("fastest")
screen = Screen()
screen.colormode(255)
colors = []
extracted_colors = colorgram.extract('image.jpg', 30)
for color in extracted_colors:
    if color.proportion < 0.18:
        colors.append(color.rgb)


def draw_dots(num_rows_cols):
    t.penup()
    t.hideturtle()
    t.setposition(num_rows_cols * -25, num_rows_cols * -25)
    for row in range(num_rows_cols):
        for col in range(num_rows_cols):
            t.dot(20, choice(colors))
            t.forward(50)
        t.setposition(num_rows_cols * -25, t.ycor() + 50 )


draw_dots(10)
screen.exitonclick()