from turtle import *
from random import randint
# Я впервые использую черепаху и знаю, что тут слишком много мусора
# Это так же связано с тем, что я уопирую и вставляю свой старый код, а не пишу каждый раз с нуля
print("[Up] - вверх\n[Down] - вниз\n[Right] - выстрел\nПрошу не нажимать после [Right] на клавиши")
speed(0)
bgcolor("black")
setx(-360)
pencolor("white")
setx(360)
setx(0)
left(90)
forward(25)
right(90)
forward(15)
right(90)
forward(25)
right(90)
forward(15)
setx(-180)
pendown
pencolor("red")
speed(2)
angle = 45
right(135)
def Up():
    global angle
    left(2.5)
    angle += 2.5
    if angle > 85:
        angle = 85
        right(2.5)
def Down():
    global angle
    right(2.5)
    angle -= 2.5
    if angle < 30:
        angle = 30
        left(2.5)
def Forward():
    global angle
    forward(200)
    right(angle*2)
    speed(0)
    for i in range(350):
        if ycor()>0 and ycor()<25 and xcor()>0 and xcor()<15:
            pencolor("yellow")
        elif ycor()<0:
            pencolor("black")
        else:
            pencolor("red") 
        forward(1)
    penup()
    forward(-350)
    left(angle*2)
    forward(-200)
    pendown()
    pencolor("red")
Screen().onkey(Up, "Up")
Screen().onkey(Down, "Down")
Screen().onkey(Forward, "Right")
Screen().listen()
mainloop()