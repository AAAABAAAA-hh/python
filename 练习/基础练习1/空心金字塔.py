# 输出一个整数 能打印改整数层的空心金字塔 并且金字塔的底层全为 *
# 思想： 化繁为简   先死后活

# 化繁为简
# 先打印一行* 》 打印五行* 》打印一个直角三角形 》打印一个实心金字塔 》 打印空心金字塔

#先死

# for i in range(5):
#     for j in range(5 - i - 1): #改正
#         print(" ",end = " ")
#     for j in range(2 * (i + 1) -1):
#         if j == 0 or j == 2 * i  or i == 5 - 1 :
#             print("*", end=" ")
#         else:
#             print(" ",end = " ")
#     print("")

# 后活  从上死改活  添加变量 n

n = int(input("请输入要打印的空心金字塔的行数："))

for i in range(n):
    for j in range(n - i - 1): #改正
        print(" ",end = " ")
    for j in range(2 * (i + 1) -1):
        if j == 0 or j == 2 * i  or i == n - 1 :
            print("*", end=" ")
        else:
            print(" ",end = " ")
    print("")

# 至此，可以控制打印的空心的金字塔的行数，此题结束。


