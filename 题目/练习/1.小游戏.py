# # 猜数字游戏
# import random
# number = random.randint(1,100)
# # print(type(number))
# print("请在1~100之间猜一个数：")
# while True:
#     gauss_number1 = int(input("请猜一个数字："))
#     # print(type(guess_number1))
#     if gauss_number1 == number:
#         print("恭喜你，猜对了，游戏结束")
#         break
#     elif int(gauss_number1) < int(number):
#         print("猜小了，请再猜一次")
#     else:
#         print("猜大了，请再猜一次：")

# 石头剪刀布
# import random
# random_list = ["剪刀","布","石头","剪刀"]
# for i in range(11):
#     computer_result = random_list[random.randint(0,2)]
#     you = input("请输入：【剪刀/石头/布】\n")
#     print(f"你出了{you},电脑出了{computer_result}",end=" ")
#     if you == computer_result:
#         print("平手")
#     elif random_list[random_list.index(you)+1] == computer_result:
#         print("win")
#     else:
#         print("lose")

# 统计字符数量--可以改写一下当做函数使用
# text  = input("请任意输入一段文字：")
# count_dict = {}
# for i in text:
#     if i not in count_dict:
#         count_dict[i] = 0
#     count_dict[i] += 1
# print(count_dict)

# 字符串加密  错
# str_text = input("请输入一段文本：")
# for i in str_text:
#     i += 2
# print(str_text)


# 字符串加密（答案）
# digits = '1234567890' * 2
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz' * 2
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
#
# text = input('请输入字符串：')
# new_text = ''
# for c in text:
#     if c in digits:
#         new_c = digits[digits.index(c) + 2]
#     elif c in ascii_lowercase:
#         new_c = ascii_lowercase[ascii_lowercase.index(c) + 2]
#     elif c in ascii_uppercase:
#         new_c = ascii_uppercase[ascii_uppercase.index(c) + 2]
#     else:
#         new_c = c
#     new_text += new_c
#
# print(f'加密后的字符串为：{new_text}')

#

