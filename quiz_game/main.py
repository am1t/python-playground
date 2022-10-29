from quiz_brain import QuizBrain

game = QuizBrain()

while game.has_more_question():
    answer = game.next_question()
    if answer == "exit":
        break

    game.check_answer(answer)

print("You have completed the quiz.")
print(f"You final score is {game.score}/{game.current_question}.")