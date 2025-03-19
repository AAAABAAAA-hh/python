import turtle as t

t.bgcolor()

t.speed(0)
t.pensize(10)
t.color('black')
t.circle(100)

t.penup()
t.color('red')
t.forward(250)
t.pendown()
t.begin_fill()
t.circle(100)

t.penup()
t.color('blue')
t.backward(250 * 2)
t.pendown()
t.begin_fill()
t.circle(100)

#125  -100

t.penup()
t.color('green')
t.goto(125,-100)
t.pendown()
t.circle(100)

t.penup()
t.color('yellow')
t.goto(-125,-100)
t.pendown()
t.circle(100)

t.exitonclick()

























































































