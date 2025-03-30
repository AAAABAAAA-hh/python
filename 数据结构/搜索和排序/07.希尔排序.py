# 递减增量排序 -> 希尔排序 需用到插入排序辅助



def insertion_sort(arr, start, gap):
    """
    对数组的特定间隔部分进行插入排序。

    param:
        arr: 要排序的数组。
        start: 起始索引。
        gap: 间隔大小。
    """
    for i in range(start + gap, len(arr), gap):
        current_value = arr[i]
        position = i
        while position >= gap and arr[position - gap] > current_value:
            arr[position] = arr[position - gap]
            position -= gap
        arr[position] = current_value

def shell_sort(arr):
    """
    希尔排序算法。

    param:
        arr: 要排序的数组。
    """
    n = len(arr)
    gap = n // 2  # 初始间隔

    while gap > 0:
        for start in range(gap):
            insertion_sort(arr, start, gap)  # 对每个子列表进行插入排序
        gap //= 2  # 缩小间隔

# 示例用法
my_list = [12, 34, 54, 2, 3, 41, 1]
shell_sort(my_list)
print("排序后的列表:", my_list)


























