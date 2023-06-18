def add (*args):
    sum = 0
    for i in args:
        sum += int(i)
    return sum

print (add(1,2,3,4,5,6,7,8))

def multiply(*args):
    product = 0
    for i in args:
        product *= i
    return product

def calculate (n, **kwargs):
    print(n)
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    return n

print (calculate(2, add=10, multiply=11))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")


mycar = Car(make="Nissan", color="white")

print(mycar.model)
print(mycar.year)
print(mycar.make)
print(mycar.color)
