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
forward(30)
right(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)
setx(-180)
pendown
pencolor("red")
speed(2)
angle = 45
right(135)
def Up():
    global angle
    left(1)
    angle += 1
    if angle > 85:
        angle = 85
        right(1)
def Down():
    global angle
    right(1)
    angle -= 1
    if angle < 45:
        angle = 45
        left(1)
def Forward():
    global angle
    forward(200)
    right(angle*2)
    speed(0)
    for i in range(300):
        if ycor()>0 and ycor()<30 and xcor()>0 and xcor()<20:
            pencolor("yellow")
            shape("circle")
            break
        elif ycor()<0:
            pencolor("gray")
            shapesize(0.5, 0.5)
            shape("triangle")
        else:
            pencolor("red") 
        forward(1)
    if ycor()<10:
        shapesize(1, 1)
        pencolor("white")
        shape("circle")
Screen().onkey(Up, "Up")
Screen().onkey(Down, "Down")
Screen().onkey(Forward, "Right")
Screen().listen()
mainloop()