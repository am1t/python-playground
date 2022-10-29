from question_bank import QuestionBank

class QuizBrain:

    def __init__(self) -> None:
        self.current_question = 0
        self.score = 0
        self.bank = QuestionBank()
        self.bank.build_question_bank()

    def next_question(self):
        return input(f"Q.{self.current_question+1}: {self.bank.questions[self.current_question].text} (True/False)?: ")

    def has_more_question(self):
        return self.current_question < len(self.bank.questions)

    def check_answer(self, user_answer):
        if self.bank.questions[self.current_question].answer == user_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("Sigh! That's incorrect.")
        
        self.current_question += 1
        print(f"Your current score is {self.score}/{self.current_question}.\n\n")
