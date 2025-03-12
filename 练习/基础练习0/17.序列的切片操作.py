# 序列的切片操作
# my_list = [0,1,2,3,4,5,6]
# result1 = my_list[1:4:1]
# print(result1)
# my_str = "01234567"
# result3 = my_str[0::2]
# print(result3)
# result4 = my_str[::-1]
# print(result4)

#切片练习     取出  ‘黑马程序员’
my_str = "四大万,员序程马黑来,收纳盒学"
# 方法一
a = my_str.split(",")[1].replace("来","")[::-1]
print(a)
my_str = my_str.split(",")[1]
# print(my_str.split(",")[1])
print(my_str)
my_str = list(my_str)
print(my_str)
my_str.reverse()
print(my_str)
my_str.remove("来")
print(my_str)
my_str = ''.join(my_str)
print(my_str)
















