# 两个词是否是重新排列组成的 以python举例
word_1 = input("输入原始字符串")
word_2 = input("输入可能的变位词")
list_1 = []
for char in word_1:
    list_1.append(char)
for j in range(len(list_1)):
    if list_1[j] not in word_2:
        print(f"{word_1}与{word_2}不是变位词")
        break
else:
        print(f"{word_1}与{word_2}是变位词")





