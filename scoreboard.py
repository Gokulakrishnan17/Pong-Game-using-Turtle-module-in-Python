from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.current_score1 = 0
        self.current_score2 = 0
        self.update()

    def update(self):
        self.goto(100, 180)
        self.write(self.current_score1, align="center", font=("Courier", 88, "bold"))
        self.goto(-100, 180)
        self.write(self.current_score2, align="center", font=("Courier", 88, "bold"))

    def r_score(self):
        self.current_score1 += 1
        self.clear()
        self.update()

    def l_score(self):
        self.current_score2 += 1
        self.clear()
        self.update()
