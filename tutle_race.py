from tkinter import Y
from turtle import Turtle, Screen
import random

turtle_attribute = [
    {
        "color": "green",
        "y-coordinate" : -70 
    },
    {
        "color": "red",
        "y-coordinate" : -40 
    },
    {
        "color": "blue",
        "y-coordinate" : -10 
    },
    {
        "color": "yellow",
        "y-coordinate" : 20 
    },
    {
        "color": "orange",
        "y-coordinate" : 50 
    },
    {
        "color": "purple",
        "y-coordinate" : 80 
    },
]

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Who will win?")

def setup_turtles():
    running_turtles = []

    for attr in turtle_attribute:
        current_turtle = Turtle(shape="turtle")
        current_turtle.color(attr["color"])
        current_turtle.penup()
        current_turtle.goto(-230, attr["y-coordinate"])
        running_turtles.append(current_turtle)
    
    return running_turtles

def reset_turtles(running_turtles):
    for current_turtle in running_turtles:
        attr = next(attr for attr in turtle_attribute if attr["color"] == current_turtle.pencolor())
        current_turtle.goto(-230, attr["y-coordinate"])

is_racing = True

running_turtles = setup_turtles()

play_again = "y"
while play_again == "y":
    while is_racing:
        for turtle in running_turtles:
            if turtle.xcor() > 220:
                winner = turtle.pencolor()
                is_racing = False
                break
            else:
                turtle.forward(random.randint(1, 10))

    if user_bet == winner:
        print(f"You win! Turtle {winner} won the race!")
        play_again = screen.textinput("You win!", f"You win! Turtle {winner} won the race! Do you want to play again? (y/n)")
    else:
        print(f"You lose! Turtle {winner} won the race!")
        play_again = screen.textinput("You lose!", f"You lose! Turtle {winner} won the race! Do you want to play again? (y/n)")
    if play_again == "y":
        reset_turtles(running_turtles)
        is_racing = True
        user_bet = screen.textinput("Make your bet", "Who will win?")

screen.exitonclick()