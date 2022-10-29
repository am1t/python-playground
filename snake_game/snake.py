import time
from turtle import Turtle

(UP, DOWN, LEFT, RIGHT) = (90, 270, 180, 0)

class Snake:
    def __init__(self) -> None:
        self.body = []
        self.draw_snake()
        self.head = self.body[0]
        self.tail = self.body[-1]

    def draw_snake(self):
        for position in [0, -20, -40]:
            self.add_segment(position)

    def add_segment(self, position):
        snake_body_part = Turtle(shape="square")
        snake_body_part.penup()
        snake_body_part.color("white")
        snake_body_part.setx(position)
        self.body.append(snake_body_part)

    def extend(self):
        self.add_segment(self.tail.xcor() - 20)

    def move_snake(self):
            for seg_num in range(len(self.body) - 1, 0, -1):
                self.body[seg_num].goto(self.body[seg_num-1].xcor(), self.body[seg_num-1].ycor())

            self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
