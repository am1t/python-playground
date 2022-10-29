import random

def play_once():
    options = ["Rock", "Paper", "Scissor"]
    user_choice = int(input("Input your choice - 0 for rock, 1 for paper and 2 for scissor "))
    computer_choice = random.randint(0, 2)
    print(f"You chose {options[user_choice]}\nComputer chose {options[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif ((user_choice - computer_choice > 0 and user_choice - computer_choice != 2) or 
        user_choice - computer_choice == -2):
        print("You win!")
    else:
        print("You Lose!")

while True:
    play_once()
    if input("Play again? y for Yes and n for No - ") == 'n':
        break