'''
Here we'll test event listeners
'''

import turtle



class SimpleDraw:
    myTurtle = turtle.Turtle()
    myScreen = turtle.Screen()

    def __init__(self) -> None:
        self.addListeners()

    def moveForward(self):
        self.myTurtle.forward(10)

    def moveBackward(self):
        self.myTurtle.backward(10)

    def turnLeft(self):
        self.myTurtle.left(90)

    def turnRight(self):
        self.myTurtle.right(90)
    
    def clear(self):
        self.myTurtle.clear()
        self.myTurtle.penup()
        self.myTurtle.home()
        self.myTurtle.pendown()

    def addListeners(self):
        self.myScreen.onkey(key="w", fun=self.moveForward)
        self.myScreen.onkey(key="s", fun=self.moveBackward)
        self.myScreen.onkey(key="a", fun=self.turnLeft)
        self.myScreen.onkey(key="d", fun=self.turnRight)
        self.myScreen.onkey(key="c", fun=self.clear)

    def run(self):
        self.myScreen.listen()
        self.myScreen.exitonclick()


myTurtle = SimpleDraw()
myTurtle.run()