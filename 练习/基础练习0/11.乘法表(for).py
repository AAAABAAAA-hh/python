
# 第一钟写法：无重复

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {j * i}\t", end="")
#     print()
#



#有重复的乘法口诀表

# 一:通过循环嵌套来实现乘法口诀表的全实现

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{j} * {i} = {j * i}\t", end="")
#     print()


# 二:用列表实现全 口诀表（想要实现没有重复的口诀表可以通过if——elif语句来控制输出语句，来消除重复的语句）
# 通过if语句来进一步消减口诀表中多余的部分、

list_1 = []
list_2 = []
for i in range(1, 10):
    list_1.append(i)
for j in range(1, 10):
    list_2.append(j)
for k in range(0, 9):
    for z in range(0, 9):
        if list_1[k] != list_2[z] + 1:
            print(f"{list_1[k]} * {list_2[z]} = {list_1[k] * list_2[z]}\t", end="")
    print()
