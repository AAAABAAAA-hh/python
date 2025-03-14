# # 使用构造器来编写类的属性
# class Person:
#     # 构造方法（构造器）
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# # 此时self 就是p1
# p1 = Person('John', 20)
# print(f"P1的信息是: 名字：{p1.name} , 年龄：{p1.age}")

#构造器的多种方式  不定长参数   以面积举例
class Rect:
    length = 0
    width = 0

#正常的构造方法
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
# 应用：
# p1 = Rect(10,20)


# # 不定长参数的构造方法
#     def __init__(self,*x):
#         if len(x) == 1:
#             self.length = x[0]
#             self.width = x[0]
#         elif len(x) == 2:
#             self.length = x[0]
#             self.width = x[1]
#     def s(self):
#         return self.length * self.width
# # 应用：
# p1 = Rect(10,100)
# print(p1.s())

# 使用@classmethod 装饰器重载构造函数
    def __init__(self, l, w):
        self.length = l
        self.width = w
    @classmethod
    def initsec(cls, l):
        return cls(l, l)
    def e(self):
        return self.width * self.length
# 使用方法和init不同
t = Rect.initsec(1)
print(t.e())
# t = Rect(2, 4)
# print(t.e())


























