from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_position = (self.xcor() + self.x_move, self.ycor() + self.y_move)
        self.goto(new_position)
        print(self.ycor())

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def ball_reset1(self):
        self.__init__()
        self.x_move *= -1
        self.y_move *= -1
        self.move()

    def ball_reset2(self):
        self.__init__()
        self.move()

    def inc_speed(self):
        self.move_speed *= 0.9
