class Animal :
    health = 100
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def breathe(self):
        print(f'{self.name} is breathing')
