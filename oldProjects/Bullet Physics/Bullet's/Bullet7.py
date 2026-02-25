from turtle import *
from random import randint
print("[Up] - вверх\n[Down] - вниз\n[Right] - выстрел\nПрошу не нажимать после [Right] на клавиши")
speed("fast")
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
pencolor("black")
forward(90)
right(90)
forward(90)
right(90)
setx(-180)
pencolor("red")
speed(2)
left(5)
def Up():
    left(5)
def Down():
    right(5)
def Forward():
    for i in range(300):
        if xcor()>0 and xcor()<45 and ycor()<90 and ycor()>-90:
            pencolor("yellow")
        else:
            pencolor("red")
        forward(1)
    speed(0)
    for i in range(17):
        if randint(0,1) == 1:
            left(x:=randint(0,180))
            forward(45)
            forward(-45)
            right(x)
        else:
            right(x:=randint(0,180))
            forward(45)
            forward(-45)
            left(x)
pencolor("red")
Screen().onkey(Up, "Up")
Screen().onkey(Down, "Down")
Screen().onkey(Forward, "Right")
Screen().listen()
mainloop()