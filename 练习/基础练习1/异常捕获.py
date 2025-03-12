age =  0
while True:
    try:
        age = int(input("请输入一个整数："))
        break
    except ValueError as e:
        print("你输入的不是整数，请重新输入。")
    
#raise 支持强制触发异常
try:
    print(110 / 0)
except ZeroDivisionError as e:
    # raise ZeroDivisionError
    print(f"触发异常：{e}")





































