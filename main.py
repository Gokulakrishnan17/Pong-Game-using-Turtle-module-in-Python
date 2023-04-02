from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
turtle = Turtle()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

turtle.penup()
turtle.hideturtle()
turtle.color("yellow")
turtle.goto(0, 300)
turtle.right(90)
for i in range(0, 31):
    turtle.pensize(5)
    turtle.speed("fastest")
    turtle.pendown()
    turtle.forward(15)
    turtle.penup()
    turtle.forward(15)

paddle1 = Paddle((350, 0), "red")
paddle2 = Paddle((-350, 0), "blue")
ball = Ball()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(key="Up", fun=paddle1.paddle_forward)
screen.onkey(key="Down", fun=paddle1.paddle_downward)
screen.onkey(key="w", fun=paddle2.paddle_forward)
screen.onkey(key="s", fun=paddle2.paddle_downward)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(paddle1) < 60 or ball.xcor() < -320 and ball.distance(paddle2) < 60:
        ball.bounce_x()
        ball.inc_speed()
    if ball.xcor() > 420:
        ball.ball_reset1()
        scoreboard.l_score()
    if ball.xcor() < -420:
        ball.ball_reset2()
        scoreboard.r_score()
screen.exitonclick()
