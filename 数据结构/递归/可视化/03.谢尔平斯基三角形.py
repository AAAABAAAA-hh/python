import  turtle as t

def draw_triangle(color, points):
    t.fillcolor(color)
    t.penup()
    t.goto(points[0][0], points[0][1])
    t.pendown()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    # 回到起点，形成闭合三角形
    t.goto(points[0][0], points[0][1])
    t.end_fill()

# 测试
# draw_triangle('red', [[0, 300], [-300, 0], [300, 0]])
def get_mid(p1,p2):
    """
    计算三角形每条线的中间点
    :param p1:输入第一个点
    :param p2: 输入第二个点
    :return: 返回两个数值 分别为x y 坐标
    """
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinskki(points,degree):
    color_map = ["blue","red","green","white","black","yellow","orange"]
    draw_triangle(color_map[degree], points)

    if degree > 0:
        sierpinskki(
            [points[0],
             get_mid(points[0],points[1]),
             get_mid(points[0],points[2])],
            degree - 1
        )
        sierpinskki(
            [points[1],
             get_mid(points[0],points[1]),
             get_mid(points[1],points[2])],
            degree - 1
        )
        sierpinskki(
            [points[2],
             get_mid(points[2],points[1]),
             get_mid(points[0],points[2])],
            degree - 1
        )


def main():
    t.speed(0)
    points = [[-100,-50],[0,100],[100,-50]]
    sierpinskki(points,5)
    t.done()

# test
main()



















