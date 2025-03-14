#                                            摆平面正方形
#定义一个可以计算开根号的函数    计算   7385137888721的开根为2717561.018398851

import math
def gen():
      n = int(input('数字:'))
      x = math.sqrt(n)
      print(x)
      print(type(x)) #开根号后的类型为float

#计算仅用2*2摆完正方形还剩余多少2*2，将其转化为1*1，比例为4 剩余lost个2*2
a = 2717561
b = a**2
print(b)
lost = 7385137888721 - b
print(lost)
#将2*2转化为1*1后，计算总剩余1*1  为lost_1
lost_1 = lost * 4 + 10470245
print(lost_1)
#在2*2摆完的基础上向外加1*1
len_1 = 2717561
z = lost_1
while z >= 0:
    z = lost_1 - (len_1 + 1) * 4 + 4
    len_1 += 1
    print(len_1)
    print(z)
print(f"答案为{len_1}")









