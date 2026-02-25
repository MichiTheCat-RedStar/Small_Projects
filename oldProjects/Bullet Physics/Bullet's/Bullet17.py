from turtle import *
from random import randint
# Я впервые использую черепаху и знаю, что тут слишком много мусора
# Это так же связано с тем, что я уопирую и вставляю свой старый код, а не пишу каждый раз с нуля
print("[Up] - вверх\n[Down] - вниз\n[Right] - выстрел\nПрошу не нажимать после [Right] на клавиши")
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
setx(200)
sety(-30)
pendown()
pencolor("white")
sety(30)
forward(30)
sety(-30)
forward(-30)
penup()
home()
setx(-180)
pencolor("red")
if randint(0,1)==0:
    left(randint(0, 45))
else:
    right(randint(0, 45))
pendown()
hit = 0
def Up():
    left(2.5)
def Down():
    right(2.5)
def Forward():
    while True:
        forward(1)
        if xcor() >= 30 and xcor() <= 75 and ycor() >= -90 and ycor() <= 90:
            break
    pencolor("lime")
    Forwards_a = 0
    while True:
        forward(1)
        Forwards_a += 1
        if xcor() <= 30 or xcor() >= 75 or ycor() <= -90 or ycor() >= 90:
            break
    global hit
    pencolor("yellow")
    for i in range(7):
        if (y:=randint(0, 1)) == 0:
            left(x:=randint(0, 1500)*0.01)
        else: # Благодаря умножению на 0.01 я сделал из randint float координаты
            right(x:=randint(0, 1500)*0.01)
        Forwards_b = 0
        for ii in range(240):
            if xcor() >= 200 and xcor() <= 230 and ycor() >= -30 and ycor() <= 30:
                hit += 1
                break
            forward(1)
            Forwards_b += 1
        penup()
        forward(-Forwards_b)
        pendown()
        if y==0:
            right(x)
        elif y==1:
            left(x)
    pencolor("lime")
    penup()
    forward(-Forwards_a)
    pendown()
    shapesize(0.5, 0.5)
    shape("circle")
    print("\nПопаданий осколков:", hit)
Screen().onkey(Up, "Up")
Screen().onkey(Down, "Down")
Screen().onkey(Forward, "Right")
Screen().listen()
mainloop()