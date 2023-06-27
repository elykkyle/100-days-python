from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle with win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

start_x = -230
start_y = -75
for color in colors:
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(start_x, start_y)
    start_y += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

finish_line = screen.window_width() / 2 - 20
winner = ''

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= finish_line:
            is_race_on = False
            winner = turtle.pencolor()

if user_bet == winner:
    print(f"You win! The {winner} turtle won the race.")
else:
    print(f"You lose. The {user_bet} turtle did not win.")
    print(f"The {winner} turtle won.")


screen.exitonclick()