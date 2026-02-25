from turtle import *
from random import randint
speed(0)
bgcolor("black")
setx(-360)
pencolor("gray")
setx(360)
penup
setx(-90)
home
pendown
left(45)
Color=0
for i in range(180):
    if Color == 0:
        pencolor("red")
    elif Color == 1:
        pencolor("orange")
    elif Color == 2:
        pencolor("yellow")
    elif Color == 3:
        pencolor("green")
    elif Color == 4:
        pencolor("blue")
    elif Color == 5:
        pencolor("indigo")
    elif Color == 6:
        pencolor("violet")
    forward(2)
    right(0.5)
    Color+=1
    if Color > 6:
        Color=0
pencolor("white")
speed(1)
right(randint(0, 25))
forward(90)
shape("circle")
end_fill()
done()