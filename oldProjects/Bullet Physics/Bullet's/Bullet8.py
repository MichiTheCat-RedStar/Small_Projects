from turtle import *
from random import randint
speed(0)
bgcolor("black")
setx(-360)
pencolor("white")
setx(360)
penup
setx(-90)
home
pendown
left(45)
pencolor("red")
for i in range(180):
    forward(2)
    right(0.5)
pencolor("yellow")
speed(1)
right(randint(0, 25))
forward(90)
shape("circle")
end_fill()
done()