from turtle import Turtle
from random import randint


victoria = Turtle()

victoria.color('red')
victoria.shape('turtle')

victoria.penup()
victoria.goto(-160, 100)
victoria.pendown()

jack = Turtle()

jack.color('blue')
jack.shape('turtle')

jack.penup()
jack.goto(-160, 70)
jack.pendown()

sophie = Turtle()

sophie.color('yellow')
sophie.shape('turtle')

sophie.penup()
sophie.goto(-160, 40)
sophie.pendown()

will = Turtle()

will.color('green')
will.shape('turtle')

will.penup()
will.goto(-160, 10)
will.pendown()

for movement in range(100):
    victoria.forward(randint(1,5))
    jack.forward(randint(1,5))
    sophie.forward(randint(1,5))
    will.forward(randint(1,5))

