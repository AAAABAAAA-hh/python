# 创建一个while循环遍历列表的函数
def list_while_func():
    my_list = ["传智教育","黑马程序员","python"]
    #循环控制变量
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的元素为：{element}")
        index += 1
        if index == len(my_list):
            print("遍历结束")
            break
#调用函数
list_while_func()

#创建一个for循环遍历列表的函数
def list_for_func():
    my_list2 = [1,2,3,4,5]
    for i in my_list2:
        print(i)
        if i == 5:
            print("遍历结束")
            break
#调用函数
list_for_func()



