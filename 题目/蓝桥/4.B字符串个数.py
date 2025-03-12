import math
Mod = 10 ** 9 + 7
totil = pow(9,10000,Mod)
# 容斥定理
totil_not_3 = pow(8,10000,Mod)
totil_not_7 = pow(8,10000,Mod)
totil_not_3_7 = pow(7,10000,Mod)
#结果：
"""
 取模公式： （a % mod）*（b % mod） = （a * b）% mod
 不使用此公式会导致数值超出范围 
 使用此公式可以有效简化时间： pow 取模
 做题时注意数值，不要超出范围
"""
result = (totil - totil_not_3 - totil_not_7 + totil_not_3_7) % Mod
print(result)

































