from turtle import *
from random import randint
print("[Up] - вверх\n[Down] - вниз\n[Right] - выстрел\nПрошу не нажимать после [Right] на клавиши")
speed(0)
bgcolor("black")
setx(-360)
pencolor("white")
setx(360)
penup
setx(-90)
home
penup
forward(90)
setx(-180)
pendown
pencolor("red")
speed(2)
angle = 45
left(45)
def Up():
    global angle
    left(5)
    angle += 5
    if angle > 90:
        angle = 90
        right(5)
def Down():
    global angle
    right(5)
    angle -= 5
    if angle < 5:
        angle = 5
        left(5)
def Forward():
    global angle
    forward(200)
    if angle > 45:
        # Попытки всё починить (не работает)
        right(angle*2-0.04*angle)
    elif angle < 45:
        right(angle*2+0.26*angle)
    else:
        right(angle*2)
    speed(0)
    for i in range(400):
        if ycor()<0:
            pencolor("black")
        forward(1)
    penup()
    forward(-400)
    if angle > 45:
        left(angle*2-0.04*angle)
    elif angle < 45:
        left(angle*2+0.26*angle)
    else:
        left(angle*2)
    forward(-200)
    pendown()
    pencolor("red")
Screen().onkey(Up, "Up")
Screen().onkey(Down, "Down")
Screen().onkey(Forward, "Right")
Screen().listen()
mainloop()