'''
This module contains the quiz class.
'''

class Quiz:
    ANSWER_RIGHT = "You got it right!"
    ANSWER_WRONG = "You got it wrong!"
    ANSWER_TIMEOUT = "You ran out of time!"


myquiz = Quiz()
print(myquiz.ANSWER_RIGHT)
print(myquiz.ANSWER_WRONG)
print(myquiz.ANSWER_TIMEOUT)
