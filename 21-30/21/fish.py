import animal

class Fish(animal.Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 10

    def swim(self):
        self.health -= 1
    
    def breathe(self):
        super().breathe()
        print(f'underwater breathing')
    

    