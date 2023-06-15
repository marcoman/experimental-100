import turtle


myturtle = turtle.Turtle()
print (myturtle)

myscreen = turtle.Screen()
myturtle.shape('triangle')
myturtle.color('green')

for i in range(50):
    myturtle.forward(200)
    myturtle.left(91)
    

myscreen.exitonclick()

