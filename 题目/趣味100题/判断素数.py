import math
number = int(input("请输入任意一个整数："))
for i in range(2,int(math.sqrt(number))):
    if number % i == 0:
        print("This number is not a prime number")
        break
# else在与for和while对应时，else含义：当循环是正常结束的时候，执行else语句
else:
    print("This number is a prime number")




