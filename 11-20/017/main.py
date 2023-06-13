'''
This class is for experimental purposes.
'''

class User(object):
    '''
    This is a test class shwoing a user class.
    '''
    def __init__(self, name, password):
        self.name = name
        self.password = password
        print(f'Initialized a new class')
        self.followers = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def set_id(self, id):
        self.id = id


class Car(object):
    '''
    This is a test class showing a car class.
    '''

    self.seats = 4

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        print(f'Initialized a new class')

    def __str__(self):
        return self.model

    def __repr__(self):
        return self.model

    def set_seats(self, seats):
        self.seats = seats


user1 = User("1", "Marco")
user2 = User(2, "Beth")
