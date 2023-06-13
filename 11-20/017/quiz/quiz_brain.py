'''
This is the question challenge problem.
'''

import data
import question_model
import opentriviadb



class QuizBrain(object):
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_number = 0

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


question_bank = []
for question in data.question_data:
    question_bank.append(question_model.Question(question['text'], question['answer']))

extra_questions = data.opentdb_data

for question in extra_questions:
    question_bank.append(question_model.Question(question['question'], question['correct_answer']))

for question in question_bank:
    print(question.question)
    print(question.answer)
    print("\n")

myquiz = QuizBrain(question_bank)
while myquiz.still_has_questions():
    myquiz.next_question()

