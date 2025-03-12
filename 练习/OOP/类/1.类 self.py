#  面向对象编程
# 定义一个Cat类,age , name,color 是属性，即成员变量



# class Cat:
#     age = None
#     name = None
#     color = None
# # 通过Cat类 ，创建 实例
# cat1 = Cat()
# # 赋值
# cat1.name = "小白"
# cat1.age = 2
# cat1.color = "write"
#
# print(f"cat1的信息为 age:{cat1.age},name:{cat1.name},color:{cat1.color}")
#
# 传参机制
# class Person:
#     age = None
#     name = None
#
# p1 = Person()
# p1.age = 20
# p1.name = "bai"
# print(p1.age)
# print(p1.name)
# print("----------------------------")
# p2 = p1
# print(p2.age)
# print(p2.name)
# print("----------------------------")
# p2.age = 30
# print(p1.age)
# print(p1.name)
# print(p2.age)
# print(p2.name)
# p2 = None
# print(p2.age)
#
# self
# class Person:
#     age = None
#     name = None
#
#     def hi(self):
#         print("hi,python")
#
#     def cal01(self):
#         result = 0
#         for i in range(1,1001):
#             result += i
#         print(result)
#
#     def cal02(self,n):
#         result = 0
#         for i in range(1,1 + n):
#             result += i
#         print(result)
#
# p = Person()
# p1 = Person()
# p.hi()
# p.cal01()
# n = input("输入要计算的数列的最终的数字")
# p.cal02(int(n))
#
# # 动态添加 方法
# def sum(n1,n2):
#     return n1 + n2
# p1.sum = sum
#
# # 不使用self 参数  使用静态方法 @staticmethod 否则不加self 方法会报错
# class Student:
#     @staticmethod
#     def sum(n1, n2):
#         return n1 + n2






































































































