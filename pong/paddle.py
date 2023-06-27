from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.shape("square")
        self.fillcolor("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setx(x_cor)
        # self.shapesize(stretch_wid=)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 260:
            self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -260:
            self.sety(new_y)
