# 基础冒泡排序
def sort_1(lst):
    for i in range(len(lst) -1 , 0 , -1 ):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# 改进： 可以通过 检查后续是否交换来选择可不可以提前终止排序
def sort_2(lst):
    for i in range(len(lst) -1 , 0 , -1 ):
        exchange = False

        for j in range(i):
            if lst[j] > lst[j+1]:
                exchange = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if not exchange:
            break


















