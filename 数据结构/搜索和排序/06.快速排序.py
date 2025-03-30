def partition(arr, low, high):
  """
  分区函数，选择最后一个元素作为基准，将数组分为两部分。

  参数：
    arr: 待排序的数组
    low: 分区起始索引
    high: 分区结束索引

  返回：
    基准元素的索引
  """
  pivot = arr[high]  # 选择最后一个元素作为基准
  i = low - 1  # i是小于基准的元素的索引

  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1


def quick_sort_recursive(arr, low, high):
  """
  递归快速排序函数。

  参数：
    arr: 待排序的数组
    low: 排序起始索引
    high: 排序结束索引
  """
  if low < high:
    pi = partition(arr, low, high)  # 获取基准元素的索引

    quick_sort_recursive(arr, low, pi - 1)  # 递归排序基准元素左侧的子数组
    quick_sort_recursive(arr, pi + 1, high)  # 递归排序基准元素右侧的子数组


def quick_sort(arr):
  """
  快速排序主函数。

  参数：
    arr: 待排序的数组
  """
  quick_sort_recursive(arr, 0, len(arr) - 1)


# 示例用法
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr)
print("排序后的数组:", arr)



























