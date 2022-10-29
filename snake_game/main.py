from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time

WALL_POSITION = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake")
screen.tracer(0)

snake = Snake()
food = Food()
board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

do_move = True

def collision_detected():
    if (snake.head.xcor() > WALL_POSITION or snake.head.xcor() < -WALL_POSITION or
        snake.head.ycor() > WALL_POSITION or snake.head.ycor() < -WALL_POSITION):
        return True
    
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            return True
    
    return False

while do_move:
    if collision_detected():
        do_move = False
        board.game_over()
        break

    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.add()
        board.increase()
        snake.extend()

screen.exitonclick()