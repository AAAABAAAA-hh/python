# # 函数的多返回值
# def test_return():
#     return 1,2
# x,y = test_return()
# print(x,y)

# 函数的传参
#         函数的
# def user_info(name,age,gander):
#     print(f"您的名字是:{name},年龄是:{age},性别是:{gander}")
#     return 0
# x = user_info("小明",18,"男")
# print(x)
# # 仅用位置传入参数
# user_info("小明",18,"男")
# # 仅用关键字传参  按序
# user_info(name = "小明",age = 18,gander = "男")
# # 仅用关键字传参  乱序
# user_info(age = 18,name = "小明",gander = "男")
# # 关键字和位置传参混用     位置传参必须在关键字参数的前面
# user_info("小明",18,gander = "男")
#
# # 缺省参数
# def user_info(name,age,gander = "男"):
#     print(f"您的名字是:{name},年龄是:{age},性别是:{gander}")
# user_info("xiaoming",age = 18)
#
#                                 不定长参数
# 位置参数
# def user_info(*args):
#     print(args)
# user_info(1,2,3,4)

# 关键字参数
# def user_info(**kargs):
#     print(kargs)
# user_info(name = "xiaoming",age = 18)

# 函数作为参数进行传递

# 定义一个函数
def test_func(computer):
    result = computer(1,2,3,8)
    print(f"computer的类型是：{type(computer)}")
    print(f"计算结果是:{result}")
# # 定义computer函数
# def computer(a,b,c,d):
#     return a+b+c+d
# test_func(computer)

# 匿名函数
test_func(lambda a,b,c,d : a*b*c*d)












