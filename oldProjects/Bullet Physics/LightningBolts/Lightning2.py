from turtle import *
from random import randint
speed(0)
bgcolor("black")
sety(-90)
pencolor("white")
left(90)
forward(180)
right(90)
forward(45)
right(90)
forward(180)
right(90)
forward(45)
penup()
home()
setx(-180)
pendown()
pencolor("blue")
x = 1
angle = 0
while x==1:
    for i in range(30):
        forward(1)
        if xcor() <= 45 and xcor() >= 0 and ycor() >= -90 and ycor() <= 90:
            shape("circle")
            shapesize(0.5, 0.5)
            x = 0
            break
    if randint(0,1)==0:
        left(y:=randint(0, 30))
        angle += y
    else:
        right(y:=randint(0,30))
        angle -= y
    if angle > 30: # Создаёт конус в котором молния двигается
        right(y:=randint(30, 60))
        angle -= y
    elif angle < -30:
        left(y:=randint(30, 60))
        angle += y
mainloop()