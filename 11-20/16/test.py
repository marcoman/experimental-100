class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person({self.name}, {self.age})"

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

me = Person("Marco", 100)
print(me)
print(repr(me))