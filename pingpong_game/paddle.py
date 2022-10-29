from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_cor, y_cor)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)
    
    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
        