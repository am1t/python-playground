import requests

class Question:
    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer

class QuestionBank:
    questions = []

    def build_question_bank(self):
        opentdb_api = "https://opentdb.com/api.php?amount=15&category=11&type=boolean"
        response_json = requests.get(opentdb_api).json()
        question_data = response_json["results"]

        for question in question_data:
            question_object = Question(question["question"], question["correct_answer"])
            self.questions.append(question_object)