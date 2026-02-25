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
angle = 5
left(5)
def Up():
    global angle
    left(5)
    angle += 5
    # Это гениально, я не знаю как додумался до этого, ранее расчёт был относительно 360г. и он не работал
    if angle > 180:
        angle = -180
def Down():
    global angle
    right(5)
    angle -= 5
    if angle < -180:
        angle = 180
def Forward():
    forward(150)
    if angle > -60 and angle < 60:
        right(angle*2)
    speed(0)
    for i in range(300):
        if xcor()>0 and xcor()<45 and ycor()<90 and ycor()>-90:
            pencolor("yellow")
        else:
            pencolor("red")
        forward(1)
pencolor("red")
Screen().onkey(Up, "Up")
Screen().onkey(Down, "Down")
Screen().onkey(Forward, "Right")
Screen().listen()
mainloop()