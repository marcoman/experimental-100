import turtle
import random
class TurtleRace:
    myturtle = turtle.Turtle()
    myscreen = turtle.Screen()
    bet = ''
    GAPSIZE = 40
    SCREEN_X = 250
    SCREEN_Y = 250

    turtles = [['Marco', 'red'],
               ['Beth', 'orange'],
               ['Xavier', 'yellow'],
               ['Zerlina', 'green'],
               ['Claudia', 'blue'],
    ]
    
    racers = []

    def __init__(self) -> None:
        self.myscreen.setup(self.SCREEN_X * 2 + self.GAPSIZE, self.SCREEN_Y * 2 + self.GAPSIZE)
        self.myturtle.hideturtle

    def addlisteners(self):
        self.myscreen.onkey(key="w", fun=self.moveForward)
        self.myscreen.onkey(key="s", fun=self.moveBackward)
        self.myscreen.onkey(key="a", fun=self.turnLeft)
        self.myscreen.onkey(key="d", fun=self.turnRight)
        self.myscreen.onkey(key="c", fun=self.clear)

    def get_bet(self):
        self.bet = self.myscreen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    
    def create_turtles(self, turtlecount):
        c = 0
        for t in self.turtles:
            newturtle = turtle.Turtle(shape='turtle')
            print(f'Creating turtle {t[0]} with color {t[1]} at {-self.SCREEN_Y + self.GAPSIZE * self.turtles.index(t)}')
            newturtle.speed('fastest') 
            newturtle.penup()
            newturtle.goto(x=-self.SCREEN_X + self.GAPSIZE,y= (self.turtles.index(t) -3 ) * self.GAPSIZE)

            # newturtle.goto(x=-self.SCREEN_X + self.GAPSIZE,y= -self.SCREEN_Y + self.GAPSIZE * self.turtles.index(t))
            # newturtle.goto(x=0,y=c * self.GAPSIZE)
            newturtle.color(t[1])
            newturtle.dot(20)
            self.racers.append(newturtle)
            c+=1

    def moveForward(self):
        self.myturtle.forward(10)

    def moveBackward(self):
        self.myturtle.backward(10)

    def turnLeft(self):
        self.myturtle.left(90)

    def turnRight(self):
        self.myturtle.right(90)

    def clear(self):
        self.myturtle.clear()
        self.myturtle.penup()
        self.myturtle.home()
        self.myturtle.pendown()

    def race(self):
        max_x = 0
        while max_x < self.SCREEN_X:
            for t in self.racers:
                t.forward(random.randint(1,10))
                max_x = max(max_x, t.xcor())

        for t in self.racers:
            if t.xcor() == max_x:
                winner = self.turtles[self.racers.index(t)][0]
                if winner == self.bet:
                    print(f'You won! {winner} is the winner!')
                else:
                    print(f'You lost! {winner} is the winner!')
                break 
       
    def run(self):
        self.create_turtles(5)
        self.get_bet()
        self.race()
        self.myscreen.listen()
        self.myscreen.exitonclick()

myrace = TurtleRace()
myrace.run()

