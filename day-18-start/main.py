from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
#
# tim.penup()
# tim.setx(-500)
# tim.pendown()
# for _ in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
screen = Screen()
screen.colormode(255)


# def draw_shape(num_sides):
#     tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     angle = 360 / num_sides
#     for side in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

def random_color():
    """Returns a tuple for rgb: (r, g, b)"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)
def random_walk(distance):
    tim.pensize(10)
    tim.speed("fastest")
    for span in range(distance):
        tim.pencolor(random_color())
        direction = choice([0, 90, 180, 270])
        tim.setheading(direction)
        tim.forward(30)

# random_walk(200)
def draw_spirograph(size_of_gap):
    tim.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        tim.setheading(tim.heading() + size_of_gap)
        tim.forward(0.1 * size_of_gap)
        tim.pencolor(random_color())
        tim.circle(100)


draw_spirograph(1)

screen.exitonclick()