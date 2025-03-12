# 1  求最大值 ··类

"""
    思路分析
    1.类名 A01
    2.方法 max（self，lst）
    3.**两种方法实现  通过实例对象来调用函数
                    通过修饰器来直接调用函数
"""

# list_1 = [1,1,2.9,-1.9,67.9]
# list_2 = [1,2,3,44,66,78.76,321.74745]
# class A01:
#     def max(self,lit):
#         return max(lit)
# # 调用  对象
# a = A01()
# print(a.max(list_1))
#
# class A02:
#     @classmethod
#     def max(cls,lit):
#         return max(lit)
# # 调用  类名
# print(A02.max(list_2))

# 2  改书的价格 b

# class Book(object):
#     def __init__(self,price):
#         self.price = price
#     def update_price(self,price):
#         if price > 150:
#             self.price = 150
#         elif price > 100:
#             self.price = 100
# # 调用  修改  也可以不传入price 直接用self.price 来代替
# book_1 = Book(200)
# print("book_1 书本原本的价格为：",book_1.price)
# book_1.update_price(book_1.price)
# print("book_1 书本修改后的价格为",book_1.price)

# 3  圆的周长和面积

# from math import pi
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def perimeter(self):
#         return 2 * self.radius * pi
#     def area(self):
#         return pi * (self.radius ** 2)
#
# # 例子
# circle_1 = Circle(6)
# print("圆的周长为",circle_1.perimeter())
# print("圆的面积为",circle_1.area())

# 4 定义 计算 类 add sub mul div
# class Cail:
#     def __init__(self,value):
#         self.value = value
#     def add(self,value):
#         return self.value + value
#     def sub(self,value):
#         return self.value - value
#     def mul(self,value):
#         return self.value * value
#     def div(self,value):
#         if value == 0:
#            return "value不能为0"
#         else:
#            return self.value / value
# 调用
# count_1 = Cail(1)
# count_2 = Cail(2)
# print(count_1.add(count_2.value))
# print(count_1.sub(count_2.value))
# print(count_1.mul(count_2.value))
# print(count_1.div(count_2.value))

# 5  music
# class Music:
#     def __init__(self,name,time):
#         self.name = name
#         self.time = time
#     def play(self):
#         print(self)
#     def inf(self):
#         print(f"该音乐为：{self.name}，时长为：{self.time}")
#
# music_1 = Music("mojito","5:20")
# music_1.play()
# music_1.inf()