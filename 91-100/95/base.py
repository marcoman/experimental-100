import turtle

class Base(turtle.Turtle):
    myscreen = turtle.Screen()
    BASE_WIDTH = 2
    BASE_STEP = 7
    BASE_SHAPE = 'triangle'
    BASE_COLOR = 'white'
    BASE_COLOR_HIT = 'red'

    def __init__(self, position, height, width):
        self.max_x = width / 2 - self.BASE_WIDTH
        self.min_x = -self.max_x
        super().__init__()

        self.speed(0)
        self.shape(self.BASE_SHAPE)
        self.color(self.BASE_COLOR)
        self.setheading(90)

        self.shapesize(stretch_wid=self.BASE_WIDTH, stretch_len=1)
        self.penup()
        self.goto(x=width/2, y=-height/2 + 20)
        print(f'x, y are {self.xcor()} {self.ycor()}')

    def add_listeners(self, function, key):
        self.myscreen.listen()
        self.myscreen.onkey(function, key)

    def move_left(self):
        new_x = self.xcor() - self.BASE_STEP
        if new_x < self.min_x:
            self.goto(self.min_x, self.ycor())
        else:
            self.goto(new_x, self.ycor())
 
    def move_right(self):
        new_x = self.xcor() + self.BASE_STEP
        if new_x > self.max_x:
            self.goto(self.max_x, self.ycor())
        else:
            self.goto(new_x, self.ycor())

    def shoot(self):
        print('shoot')
        
        # Show a missle

    def setup_base(self):
        pass
