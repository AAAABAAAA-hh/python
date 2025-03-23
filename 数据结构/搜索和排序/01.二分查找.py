#二分查找
def binary_search(list_1, date):
    """
    使用二分查找在有序列表中查找日期。

    参数：
        list_1: 有序列表
        date: 要查找的日期

    返回：
        如果找到日期，则返回 True，否则返回 False。
    """
    left = 0
    right = len(list_1) - 1

    while left <= right:
        mid = (left + right) // 2
        if list_1[mid] == date:
            return True
        elif list_1[mid] < date:
            left = mid + 1
        else:
            right = mid - 1

    return False


def binary_search_recursive(list_1, date, left, right):
    """
    使用递归在有序列表中查找日期。

    参数：
        list_1: 有序列表
        date: 要查找的日期
        left: 搜索范围的左边界
        right: 搜索范围的右边界

    返回：
        如果找到日期，则返回 True，否则返回 False。
    """

    if left > right:
        return False

    mid = (left + right) // 2

    if list_1[mid] == date:
        return True
    elif list_1[mid] < date:
        return binary_search_recursive(list_1, date, mid + 1, right)
    else:
        return binary_search_recursive(list_1, date, left, mid - 1)

# 使用示例
my_list = [1, 3, 5, 7, 9]
date_to_find = 5

if binary_search_recursive(my_list, date_to_find, 0, len(my_list) - 1):
    print(f"{date_to_find} 在列表中找到。")
else:
    print(f"{date_to_find} 未在列表中找到。")





















































