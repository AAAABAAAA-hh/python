import turtle as t

t.penup()
t.goto(-500, 500)
t.pendown()
def spiral(line_len):
    t.speed(0)
    if line_len > 0:
        t.forward(line_len)
        t.right(90)
        spiral(line_len - 5)

    t.hideturtle()
    t.done()

# test
spiral(1000)













































