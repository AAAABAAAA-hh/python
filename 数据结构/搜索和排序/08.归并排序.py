"""
分治策略
不使用切片操作时 时间复杂度 为 O（n * logn）
想要替代切片操作只需要在函数调用时传入头和尾坐标即可
此方法会使用额外的空间 属于牺牲空间换取时间
"""

def merge_sort(lst):
    print("Splitting",lst)
    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)
    i,j,k = 0,0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k = k + 1

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k = k + 1
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k = k + 1
    print("Merging",lst)





























