#员工编号有20名
import random
sum_1 = 10000
for i in range(1,21):
    #随机生成数字，选择领取奖金的员工
    num = random.randint(1,10)
    #if 条件判断
    if num >= 5:
        if sum_1 >= 1000:
              print(f"第{i}名员工，领取一千元")
              sum_1 -= 1000
        else:
            print(f"第{i}名员工钱已发完，结束发工资")
            break
    else:
        print(f"第{i}名员工绩效分为{num}分，没有工资")
        continue
print(f"公司余额剩余{sum_1}")





































































