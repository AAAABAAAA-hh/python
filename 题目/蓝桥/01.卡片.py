# count = 0
# for i in range(9999):
#     j = str(i)
#     char_list = [char for char in j]
#     # print(char_list)
#     count_1 = count_1 + len(char_list)


#答案
def can_form_number(n, cards):
    # 将数字n转换为字符串，以便逐位检查
    str_n = str(n)
    # 对于每一位数字，检查卡片是否足够
    for digit in str_n:
        if cards[int(digit)] <= 0:
            return False
        # 如果当前数字不是0，减少相应数字的卡片数量
        if digit != '0':
            cards[int(digit)] -= 1
    # 如果所有数字都检查完毕，返回True
    return True

def max_number(cards):
    max_num = 0
    while True:
        # 检查是否可以形成当前数字
        if can_form_number(max_num + 1, cards):
            max_num += 1
        else:
            break
    return max_num

# 初始化卡片数量，0到9各2021张
cards = [2021] * 10
# 计算小蓝能拼到的最大数
max_num = max_number(cards)
print(max_num)























