# 分隔字符串

a = input("请输入一串数据，用空格隔开：").split()

# 同时输入多个数据并同时转换为整数

a, b = map(int, input("输入一串整数，用空格分隔").split())

# map函数   map(function,iterable) 通常与lambda 匿名函数相连使用

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
map_1 = map(lambda x: x ** 2, list_1)
print(list(map_1))











