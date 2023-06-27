from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

import json
import requests


OPENTDB_URL = 'https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean'
question_bank = []

def get_question_data():
    response = requests.get(url=OPENTDB_URL)
    # print (response.json())
    return response.json()['results']


def load_online_questions():
    question_bank = []
    question_data = get_question_data()
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    return question_bank

# question_bank =  get_question_data()
question_bank = load_online_questions()
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
