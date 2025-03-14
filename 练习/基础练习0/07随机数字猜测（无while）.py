import random
num = random.randint(1,10)
guess_num=int(input("第一次输入你想的数字："))
if guess_num==num:
    print("恭喜你，第一次就猜对了")
else:
    if guess_num>num:
        print("数字大了")
    else:
        print("输入的数字小了")
    guess_num=int(input("第二次输入你所想的数字："))
    if guess_num==num:
        print("恭喜你第二次猜对了")
    else:
        if guess_num>num:
           print("输入的数字大了")
        else:
           print("输入的数字小了")
        guess_num=int(input("请第三次输入你所想的数字："))
        if guess_num==num:
           print("恭喜你，猜对了")
        else:
            print("抱歉，三次都猜错啦，请下次再来")
































