import random
num = random.randint(1,100)
i=0
guess_num = int(input("请输入所猜数字"))
while guess_num > num:
    print("猜大了，请再猜一次：")
    guess_num = int(input("请再次输入数字："))
    i += 1
while guess_num < num:
    print("猜小了，请再猜一次")
    guess_num = int(input("请再次输入数字："))
    i += 1
else:
     print("恭喜你猜对了")
     print(i)


































