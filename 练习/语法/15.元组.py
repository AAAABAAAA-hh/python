#定义元组
t1 = (1,"hello",True)
t2 = ()
t3 = tuple()
print(f"元组t1的类型是{type(t1)},内容是{t1}")
print(f"元组t2的类型是{type(t2)},内容是{t2}")
print(f"元组t3的类型是{type(t3)},内容是{t3}")

#定义单个元素
t4 = ("hello")
print(type(t4))
t4 = ("hello",)
print(type(t4))

#元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(t5)

#下标索引取出内容
num = t5[1][1]

#index查找方法
t6 = ("传智教育","黑马程序员","python")
num_1 = t6.index("黑马程序员")
print(f"查找的下标为{num_1}")
#
#count统计元素
t7 = ("传智教育","黑马程序员","黑马程序员","黑马程序员","python")
num_2 = t7.count("黑马程序员")
print(num_2)

#len计算长度
num_3 = len(t7)
print(num_3)

#元组的修改
t9 = (1,2,["itheima","itcast"])
print(f"t9的内容是{t9}")
a = t9[2][0].title()
print(a)
t9[2][0] = "黑马程序员"
print(t9)























































