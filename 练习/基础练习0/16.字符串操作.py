#定义一个字符串
from calendar import firstweekday

my_str = "itheima and itcast"

#通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串中取出的第二个元素为 {value}，取出的倒数第二个元素为 {value2}")

#index方法
num = my_str.index("and")
print(num)

#字符串替换：将字符串1换为字符串2:字符串.replace(字符串1，字符串2)
new_my_str = my_str.replace("it","程序")
print(f"将字符串 {my_str} 替换为 {new_my_str}")

#字符串的分割   语法:字符串.split(分隔符字符串)
my_str = "hellp world"
my_str_list = my_str.split(" ")
print(f"将字符串 {my_str} ，进行分割后得到 {my_str_list}，他的类型是 {type(my_str_list)}")
# 将字符串 hellp world ，进行分割后得到 ['hellp', 'world']，他的类型是 <class 'list'>

#字符串的规整操作   语法：字符串.strip(字符串)
my_str = " 1,2,3 "
print(my_str.strip())
my_str2 = "12heima21"
print(my_str2.strip("12"))
my_str3 = "12heima231"
print(my_str3.strip("12"))

#统计某元素出现次数   count
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串中 it 出现的次数是{count}")
#统计字符串的长度     len
length = len(my_str)
print(f"my_str字符串的长度是{length}")

#练习案例
first_str = "itheima,itcast,itun"
num_1 = first_str.count("it")
num_2 = first_str.replace(" ","|")
num_3 = first_str.split("|")
print(num_2,type(num_2))
print(num_3,type(num_3))
print(num_1)





