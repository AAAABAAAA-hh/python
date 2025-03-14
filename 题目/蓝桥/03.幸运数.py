import time

count = 0
time_1 = time.time()

for i in range(1000000001):
    sum_1 = 0
    sum_2 = 0
    con = len(str(i))
    mid = int(con / 2)
    if con % 2 == 0:
        list_1 = [int(d) for d in str(i)]
        for j in range(mid):
            sum_1 = sum_1 + list_1[j]
        for z in range(mid, con ):
            sum_2 = sum_2 + list_1[z]

        if sum_1 == sum_2:

            count += 1
print(count)  # 结果为 4430091  运行时间太慢
time_2 = time.time()
print(time_2 - time_1)#计算运行所需要的时间 382.12356448173523s
print(382.12356448173523 / 60) # 需要6.368726074695587分钟








































