#                     字符串扩展知识
#                     字符串驻留机制
# id（）方法 查找变量的存储地址
import sys

str_1 = "hello"
str_2 = "hello"
str_3 = "hello,world"
print(id(str_1))
print(id(str_2))
print(id(str_3))

str_4 = "#123"
str_5 = "#123"
print(id(str_4), id(str_5))
str_6 = "abc"
str_7 = "".join(["a", "b", "c"])
print(str_7)
print(id(str_6), "\n", id(str_7))

# 强制将两个字符串指向指向同一个对象    先导入sys库 语法：要改变的变量 = sys.intern(变量)
import sys

str_2 = sys.intern(str_1)

a = bin(2)
print(a)