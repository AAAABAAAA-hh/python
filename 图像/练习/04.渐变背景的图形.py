# 绘制渐变黑色背景
import turtle as t

from setuptools.windows_support import hide_file

t.speed(0)
t.colormode(255)
t.pensize(150)
t.bgcolor(0,0,0)
a, b, c = 0, 0, 0
x,y = -500,330
for i in range(6):
    t.color(a,b,c)
    a += 10
    b += 10
    c += 10
    t.penup()
    t.goto(x,y)
    y -= 150
    t.pendown()
    t.forward(1000)


# 随机生成 随机颜色的气球
from random import randint

for i in range(10):
    x = randint(-400, 300)
    y = randint(100, 300)
    a = randint(50, 255)
    b = randint(50, 255)
    c = randint(50, 255)
    t.pensize(5)
    t.color(a,b,c)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.right(90)
    t.forward(20)
    t.left(90)

t.pensize(10)
t.color("blue")
t.penup()
t.goto(-200,-100)
t.pendown()

t.write("李彦清❥(^_-)",font=('zhengkai',50))
t.hideturtle()
t.done()




 








