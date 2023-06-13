'''
This is a question class for an exercise.  We'll use it to drive questions
'''



class Question(object):
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text

questions = [
            ["What is your name?", "My name is John"],
            ["What is your favorite color?", "My favorite color is blue"],
            ["What is your favorite animal?", "My favorite animal is a dog"],
            ["What is your favorite band?", "My favorite band is the Beatles"],
]


question1 = Question("What is your name?", "My name is John")
question2 = Question("What is your favorite color?", "My favorite color is blue")
question3 = Question("What is your favorite animal?", "My favorite animal is a dog")
question4 = Question("What is your favorite band?", "My favorite band is the Beatles")

