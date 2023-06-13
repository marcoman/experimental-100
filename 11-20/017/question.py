'''
This is a question class for an exercise.  We'll use it to drive questions'''



class Question(object):
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text


