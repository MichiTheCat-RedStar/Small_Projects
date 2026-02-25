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
setx(200)
pendown()
sety(-90)
pencolor("white")
sety(90)
forward(45)
sety(-90)
forward(-45)
penup()
home()
setx(-180)
pencolor("red")
pendown()
if randint(0, 1) == 0:
    left(randint(0, 250)*0.1)
else:
    right(randint(0, 250)*0.1)
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
hit = 0
pencolor("yellow")
for i in range(25):
    if (y:=randint(0, 1)) == 0:
        left(x:=randint(0, 3000)*0.01)
    else: # Благодаря умножению на 0.01 я сделал из randint float координаты
        right(x:=randint(0, 3000)*0.01)
    Forwards_b = 0
    for ii in range(240):
        if xcor() > 200 and xcor() < 245 and ycor() > -90 and ycor() < 90:
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
mainloop()