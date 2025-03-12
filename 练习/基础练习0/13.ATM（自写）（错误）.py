#先写出前台服务
print("欢迎来到银行自助服务")
name = input("请输入您的姓名：")
money = 50000000
business = input("选择办理的业务：query_money deposit  withdraw ")

#定义四个函数
def query_money():
    print(money)
    return money
def deposit(x):
    return  f"本次存取余额为{deposit(x)}"
def withdraw(y):
    return f"本次取款余额为{withdraw(y)}"
def main():
    print("query_money")
    print("deposit")
    print("withdraw")
    global business
    print(business)
#调用函数
if name != 0:
    if business == "query_money":
        query_money()
        print(main())

    elif business == "deposit":
        a = float(input("输入存钱数："))
        deposit(a)
        print(f"你的余额为{money+float(a)}")
        print(main())

    else:
        b = input("请输入取钱数：")
        withdraw(b)
        print(f"你的余额为{money-float(b)}")
        print(main())

else:
    print("查无此人")


















































