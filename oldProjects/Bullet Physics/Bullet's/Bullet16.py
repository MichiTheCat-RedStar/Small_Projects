from turtle import *
from random import randint
speed(0)
bgcolor("black")
setx(30)
sety(-90)
pencolor("white")
sety(90)
forward(45)
sety(-90)
forward(-45)
penup()
setx(135)
pendown()
sety(-90)
pencolor("white")
sety(90)
forward(45)
sety(-90)
forward(-45)
penup()
home()
setx(-90)
pencolor("red")
pendown()
if randint(0, 1) == 0:
    left(randint(0, 25))
else:
    right(randint(0, 25))
while True:
    forward(1)
    if xcor() > 30 and xcor() < 75 and ycor() > -90 and ycor() < 90:
        break
pencolor("lime")
Forwards_a = 0
while True:
    forward(1)
    Forwards_a += 1
    if xcor() < 30 or xcor() > 75 or ycor() < -90 or ycor() > 90:
        break
pencolor("yellow")
for i in range(16):
    if (y:=randint(0, 1)) == 0:
        left(x:=randint(0, 30))
    else:
        right(x:=randint(0, 30))
    Forwards_b = 0
    for ii in range(180):
        if xcor() > 135 and xcor() < 180 and ycor() > -90 and ycor() < 90:
            break
        forward(1)
        Forwards_b += 1
    forward(-Forwards_b)
    if y==0:
        right(x)
    elif y==1:
        left(x)
pencolor("lime")
forward(-Forwards_a)
shape("circle")
shapesize(0.5, 0.5)
mainloop()