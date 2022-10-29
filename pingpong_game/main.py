import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
board = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.03)
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce()

    if ball.xcor() > 375 or ball.xcor() < - 375:
        if ball.xcor() > 375:
            board.left_scored()
        elif ball.xcor() < - 375:
            board.right_scored()
        else:
            pass

        ball.goto(0, 0)
        ball.x_move *= -1

    if right_paddle.distance(ball) < 30 or left_paddle.distance(ball) < 30:
        ball.rebound()

screen.exitonclick()