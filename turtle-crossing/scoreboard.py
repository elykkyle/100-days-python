from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-335, 273)
        self.level = 1
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def increment_level(self):
        self.level += 1
        self.show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)
