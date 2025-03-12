#  统计经过梅森旋转算法随机出的97的次数

from random import randint as r


count = 0
while True:
    a = r(1, 100)
    if a == 97:
        break
    else:
        print(a)
        count += 1
print(a)
print(f"当a = 97时，一共循环了{count + 1}次")

# break 后， 值的问题

for num in range(1, 100):
    if num > 20:
        break
print(num)

# 登录三次

for i in range(1 , 4):
    name = input("请输入你的用户名：")
    passward = input("请输入你的密码：")
    if name == "张无忌" and passward == "666666":
        print("正确")
        break
    else:
        print("请再输入一次密码及账户")

# 编程题一  计算能经过多少次路口

money =  100000
count =  0
while money > 0:
    if money > 50000:
        money = money - money * 0.05
        count += 1
    else:
        money = money - 1000
        count += 1
if money == 0:
    print(f"可以经过{count}次路口。")
else:
    print(f"可以经过{count - 1}次路口。")


# 函数  求从一加到n的和

def caoe(n):
    sum_1 = 0
    for i in rnage(1,n):
        sum_1 += i
    return sum_1

# 函数章节
# 传参方式：默认 关键字 缺省 不限 （四种方式）
# 匿名函数： lambda函数 一行 参数只作用在这一行 作用于限定
# 调用函数库


# 函数的递归调用机制
def test(n):
    if n > 2:
        test(n-1)
    print("n = ",n)

test(4)

# 用函数解决 阶乘问题的递归
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# 求n所对应的斐波那契数 使用递归方法

def fnb(n):
    """
    功能：返回n所对应的斐波那契数。
    :param n:接收所需的第n个斐波那契数。
    :return:斐波那契数
    """
    if  n ==1 or n == 2:
        return 1
    else:
        return  fnb(n-1) + fnb(n-2)

# 猴子吃桃问题 递归
"""
思路分析：
递归思想：从已知推未知 已知day10 有 1个桃子
则： day10  一个桃子
    day 9  （day10的桃子+ 1）*2
    day 8  （day9的桃子 + 1）*2
    …………
"""
def peach(n):
    if n == 10:
        return 1
    else:
        return (peach(n+1) + 1) * 2

peach_9 = peach(9)
print(peach_9)
peach_8 = peach(8)
print(peach_8)

# # 河内塔模型 递归
def hanoi_tower(num, a, b, c):
    """
    功能：完成将num个盘子从a盘转移到c盘，大盘不能在小盘上边，小盘只能在上边。
    :param num: 盘子的数量
    :param a: a柱子
    :param b: b柱子
    :param c: c柱子
    :return: 最少需要经过几次才能完全转移完成
    """
    if num == 1:
        print("第一个盘: ",a,"->",c)
    #否则就需要多次计算 运用递归方法
    else:
        # 先认为只有两个盘，上面所有的盘算一个，最下面的算一个
        # 移动上面所有盘到b柱子，中间会用到c柱子
        hanoi_tower(num - 1, a, c, b)
        # 经过上述操作会将除最下面的盘全部移动的b柱子，此时移动最下面的盘到c
        #这个最下面的盘，经过函数递归，除了第一个盘，剩下的所有都会成为最后一个盘被移动，
        print(f"第{num}个盘从: {a} -> {c}")
        #将目前b柱子上的所有盘移动到c柱子，中间会用到a柱子
        hanoi_tower(num - 1, b, a, c)

hanoi_tower(2,'A','B','C')


#将函数作为参数传递
def get_max_val(num1,num2):
    max_val = num1 if num1 > num2 else num2
    return max_val

def f1(fun,num1,num2):
    """
    功能:调用fun函数返回num1和num2中的最大值
    :param fun: 被调用的函数名
    :param num1: 传入的第一个参数
    :param num2: 传入的第二个参数
    :return: 两个参数中的最大值
    """
    return fun(num1,num2)

def f2(fun,num1,num2):
    """
    功能：返回两个参数的和以及两个参数中的最大值。
    :param fun: 被调用的函数名
    :param num1: 传入的第一个参数
    :param num2: 传入的第二个参数
    :return: 两个数的和以及两者中的最大值
    """
    return  num1 + num2,fun(num1,num2)

# # 调用测试
print(f1(get_max_val,20,30))
print(f2(get_max_val,20,30))

#lambda匿名函数（anonymous）  临时创建一个函数，只能使用一次，只能写一行
# 函数的作用域  global来转化局部变量转变为全局变量 global关键字是在函数内使用函数外定义的变量

# 对print的探究
a = 10
b=20
print("输入a的值",a,"\n输入b的值",b)

# 数据容器
list1 = ["我",123,[1,2,"shdui"]]
list2 = ["我21",122313,[1,2,"shdui"]]
list1[2][2] = "whudai"
print(list1)
print(list2)
internal_list = [1, 2]
list1 = [internal_list, 10]
list2 = [internal_list, 15]
print(list1[0] is list2[0])  # 输出 True，它们包含相同的列表对象
# 改变list1中的可变对象会影响list2
list1[0].append(3)
print(list1,id(list1[0]))  # 输出 [[1, 2, 3], 10]
print(list2,id(list2[0]))  # 输出 [[1, 2, 3], 15]，list2也发生了变化

# 列表推导式
# 生成一个一到十平方的列表
list1 = [ele**2  for ele in range(1, 11)]
print(list1)

# 字符串常用方法
# 使用ord查询一个字符的编码值
print(ord('张'))#24352
print(ord('宇'))#23431
print(ord('航'))#33322

# 切片操作

# 集合操作

# 一：练习：存储员工的信息
list_num = [1001,1002]
list_imo = [{"age":18,"name":"小明","entry_time":2023-1-1,"sal":12000},{"age":30,"name":"明","entry_time":2000-1-1,"sal":120000}]

dict_fam = {num : imo for num , imo in zip(list_num, list_imo) }
print(dict_fam)
#对每个员工工资增加20%
for key in dict_fam.keys():
    dict_fam[key]["sal"] = dict_fam[key]["sal"] * 1.2
print(dict_fam)

# 顺序查找
#通过for--else  if 语法即可
#

# 二分查找
my_list = [1,8,10,89, 1000, 1234]
def search(my_list,find_number):
    left = 0;
    right = len(my_list)-1
    while left <= right:
        mid = (left+right)//2
        if my_list[mid]  < find_number:
            left = mid+1
        elif my_list[mid] > find_number:
            right = mid-1
        else:
            return mid
    else:
        return -1
# 测试函数
index = search(my_list,8)
print(index)

# 断点调试
# f8：逐行进行代码
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

# 从一到十三中随机取出一个数
import random
a = random.randint(1,14)
print(a)

# 模块内容实例演示
# 调用创建的模块中的hi函数

from module_pre import my_module_hi
my_module_hi.hi()





































































































































































