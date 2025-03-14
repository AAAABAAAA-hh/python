# print(type(666))
# string_type=type("666")
# print(string_type)
# print(type("heima"))
# print(type(13.23))
#
# num_str=str(11)
# print(num_str,type(num_str))
from socket import fromfd

#浮点数精度缺失实验

# 精度缺失
b = 8.1 / 3
print(b)

# 解决方法  引用Decimal类
from decimal import Decimal
b = Decimal("8.1") / Decimal("3")
print(b)


