from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed("fastest")
        self.color(color)
        self.goto(position)

    def paddle_forward(self):
        if self.ycor() < 240:
            self.forward(50)

    def paddle_downward(self):
        if self.ycor() > -240:
            self.backward(50)


