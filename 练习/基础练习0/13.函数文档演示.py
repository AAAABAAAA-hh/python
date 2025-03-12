# #定义函数，进行文档说明
# def add(x,y):
#     """
#     add函数可以接收两个参数，并进行求和
#     :param x: 形参x表示相加的其中一个数字
#     :param y: 形参y表示另一个相加的数字
#     :return: 返回值是两束相加的结果
#     """
#     result = x + y
#     print(f"两数相加的结果是{result}")
#     return result
# #调用函数
# add(5,6)


#函数的调用
def fun_b():
    print("----2-----")
def fun_a():
    print("----1-----")
    #嵌套调用
    fun_b()
    print("----3-----")
    return 0
fun_a()















































































