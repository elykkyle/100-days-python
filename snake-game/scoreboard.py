from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.sety(280)
        self.update_scoreboard()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as data:
            return int(data.read())

    def set_high_score(self):
        new_high_score_string = str(self.high_score)
        with open("data.txt", 'w') as data:
            data.write(new_high_score_string)

    # def game_over(self):
    #     self.sety(0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
