import turtle
from turtle import *
t = Turtle()
t.speed(10)

""" def message(input):
    print(input)
message("Hello Class") """

t.shape('turtle')

""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200) """

""" def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200) """

""" def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right() """

""" def rectangle(x):
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
rectangle(200) """
""" def equal(x):
    t.forward(90)
    t.left(120)
    t.forward(90)
    t.left(120)
    t.forward(90)
equal(50)  """

""" for i in range(4):
    t.forward(100)
    t.left(90) """
#answers for loop.md


""" def triangle(x):
    for i in range(3):
        t.forward(x)
        t.left(120)
    

def tri():
    size = 50
    for i in range(60):
        triangle(size)
        size += 5
tri() """

def square(x):
    for i in range(4):
        t.forward(x)
        t.left(90)

""" def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 1.5
doubleSquares(5)

def addsquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25 
addsquares(5)   """

for square in range(60):
    size = 40
    square(size)
    size += 10




turtle.done