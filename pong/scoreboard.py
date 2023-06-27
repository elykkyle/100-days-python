from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.setposition(0, 220)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"{self.l_score}     {self.r_score}", align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.print_score()

    def r_point(self):
        self.r_score += 1
        self.print_score()
