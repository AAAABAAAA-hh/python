#先建立一个常规列表列表下标依次为0,1,2,3,4

my_list = ["itcast","itheima","python"]

#查找元素下标，语法：列表.index（元素）
index = my_list.index("itheima")
print(f"itheima在列表中的下标索引是：{index}")

#如果查找不存在会报错

# index_1 = my_list.index("000")
# print(f"000在列表中的下标索引是：{index_1}")

#修改特定下标索引值
my_list[0] = "传智教育"
print(f"列表被修改元素值后：{my_list}")

#在列表指定位置插入元素
my_list.insert(1,"best")
print(f"列表插入元素完成后{my_list}")

#追加末尾元素  语法：列表.append(单个元素)
my_list.append("黑马程序员")
print(f"列表追加元素完成后{my_list}")

#追加末尾元素  语法：列表.extend（其它数据容器）
my_list2 = [1,2,3]
my_list.extend(my_list2)
print(f"列表在追加了一个新的列表后结果是：{my_list}")

#删除元素  语法1：del列表[下标]
del my_list[2]
print(f"删除下标2的元素后是：{my_list}")

#删除元素  语法2：列表.pop(下标)
my_list =  ["itcast","itheima","python"]
element = my_list.pop(2)
print(f"通过pop方法取出元素后为{my_list}，取出的元素是{element}")

#直接删除指定元素  语法：列表.remove（元素）
my_list =  ["itcast","itheima","itheima","python"]
my_list.remove("itheima")
print(f"通过remove方法删除元素后为{my_list}")

#清空列表  语法：列表clear（）
my_list.clear()
print(f"通过clear之后的列表{my_list}")

#统计某元素在列表中的数量
my_list =  ["1","2","2","3"]
count_2 = my_list.count("2")
print(f"统计的元素2的数量为为{count_2}个")

#统计列表中一共有多少个元素   语法：len(列表)
my_list = [1,2,3,2,3,1,5,6,2,6]
length = len(my_list)
print(length)

#探究列表内的元组可不可以被修改
my_list_tuple = [1,1,(4,5,6)]
# my_list_tuple[2][1] = 9
print(my_list_tuple)
print("列表中的元组不能被修改")
my_list_tuple[2] = list
print(my_list_tuple)

# 
you_list = [[1,2],3,4]
you_list.reverse()
print(you_list)
#
you_list2 = ['a','c','b']
you_list2.sort(reverse = True)
print(you_list2)

#
you_list3 = [1,2,5,3,4]
you_list3.sort(reverse = True)
print(you_list3)




















