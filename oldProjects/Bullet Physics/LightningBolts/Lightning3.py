from turtle import *
from random import randint
speed(0)
bgcolor("black")
setx(345)
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
setx(-390)
pendown()
pencolor("blue")
x = 1
angle = 0
while x==1:
    for i in range(randint(35, 50)): # Для разной длинны шага молнии добавлен рандом, не советую ставить менее 30, так как тогда молния выглядит слишком плавно
        forward(1)
        if xcor() <= 390 and xcor() >= 345 and ycor() >= -90 and ycor() <= 90:
            shape("circle")
            shapesize(0.5, 0.5)
            x = 0
            break
    if randint(0,1)==0:
        left(y:=randint(0, 30))
        angle += y
    else:
        right(y:=randint(0, 30))
        angle -= y
    if angle > 45:
        right(y:=randint(45, 90)) # В randint первое число должно быть равно углу конуса, а второе - углу умноженному на два, я бы мог сделать это иначе, записывая данные в переменную, но не вижу смысла, если игрок не должен на это влиять
        angle -= y
    elif angle < -45:
        left(y:=randint(45, 90))
        angle += y
mainloop()