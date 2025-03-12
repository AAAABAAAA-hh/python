# 输入一个整数，使程序能打印出此整数所代表的行数的空心菱形。
# 思想： 化繁为简 先死后活

# 先打印9行 * 》 打印实心菱形 》 空心菱形
# 先打印上层空心三角，再打印下层空心三角，将其拆成两个空心三角形分别打印。

# 方法一  按边打印
a = int(input("请输入菱形每条边星星的个数："))
b = a
c = a
print(" " * (a - 1), "*")
for i in range(2, a + 1):  # 先打印正三角，由空格和*根据规律组成
    print(" " * (b - 1) + "*" + " " * (2 * i - 3) + "*")
    b -= 1
    if i == a:  # 临界点，当打印到此，开始打印倒三角
        for y in range(2, a):
            print(" " * y + "*" + " " * (2 * c - 5) + "*")
            c -= 1
        print(" " * a + "*")

# 方法二 按行打印
# 打印空心等菱形，这里去掉if-else条件判断就是实心的
rows = int(input("请输入空心菱形的行数："))
while rows % 2 == 0:
    rows = int(input("请输入一个奇数："))
for i in range(rows % 2 + 1):
    for j in range(rows % 2 + 1 - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# 菱形的下半部分
for i in range(rows // 2 + 1):
    for j in range(i):
        print(" ", end=" ")

    for k in range(2 * (rows // 2 + 1 - i) - 1):

        if k == 0 or k == 2 * (rows // 2 + 1 - i) - 2:
            print("*", end=" ")
        else:
            print(" ", end="")
    print()

# 多学多练多看多做
