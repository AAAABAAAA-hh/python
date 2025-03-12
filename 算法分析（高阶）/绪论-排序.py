# 插入排序法

chaos_list = [1,2,8,56,40,51,45,52,54,46,64,3]
for i in range(1, len(chaos_list)):
    value = chaos_list[i]
    j = i - 1
    while j >= 0 and chaos_list[j] > value:
        chaos_list[j + 1] = chaos_list[j]
        j -= 1
    chaos_list[j + 1] = value
print(chaos_list)

# 选择排序法

chaos_list = [1, 2, 8, 56, 40, 51, 45, 52, 54, 46, 64, 3]

for i in range(len(chaos_list)):
    min_index = i
    for j in range(i + 1, len(chaos_list)):
        if chaos_list[j] < chaos_list[min_index]:
            min_index = j
    # 交换最小值到当前位置
    chaos_list[i], chaos_list[min_index] = chaos_list[min_index], chaos_list[i]

print(chaos_list)

#                                   总结
'''
    在不用容器特定语法情况下：
    在对有序容器进行排序时，要使用下标进行换位以及比对。
    不要去管具体值的大小，值只在比较时，才会用到。
    要适应直接对下标的交换与改变。
    从整体把握整个题目，理清逻辑关系。
    不要盲目直接边想边写！！！
    不要盲目直接边想边写！！！
    不要盲目直接边想边写！！！
'''




