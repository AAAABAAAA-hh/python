#    优先队列

import heapq

class PriorityQueue:
    def __init__(self):
        self._heap = []

    def is_empty(self):
        return not self._heap

    def push(self, priority, item):
        """将带有给定优先级的元素压入队列。
        优先级越低，优先级越高。
        """
        heapq.heappush(self._heap, (priority, item))

    def pop(self):
        """移除并返回具有最低优先级的元素。
        如果队列为空，则引发 IndexError。
        """
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self._heap)[1]  # 返回元素，忽略优先级

    def peek(self):
        """返回具有最低优先级的下一个元素，但不移除它。
        如果队列为空，则引发 IndexError。
        """
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self._heap[0][1]  # 返回元素，忽略优先级

    def peek_priority(self):
        """返回最低优先级，但不移除元素。
        如果队列为空，则引发 IndexError。
        """
        if self.is_empty():
            raise IndexError("peek_priority from empty priority queue")
        return self._heap[0][0]

    def __len__(self):
        return len(self._heap)

# 示例用法：
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(3, "任务C")
    pq.push(1, "任务A")
    pq.push(2, "任务B")
    pq.push(1, "任务A2")

    print(f"队列是否为空: {pq.is_empty()}")
    print(f"队列长度: {len(pq)}")
    print(f"优先级最高的任务 (peek): {pq.peek()}")
    print(f"最高优先级 (peek_priority): {pq.peek_priority()}")

    while not pq.is_empty():
        item = pq.pop()
        print(f"处理任务: {item}")



#            堆排序

def heap_sort(lst):
    """使用堆排序对列表进行升序排序。"""
    heapq.heapify(lst)  # 将列表原地转换为最小堆
    sorted_lst = [heapq.heappop(lst) for _ in range(len(lst))]
    return sorted_lst

def heap_sort_descending(lst):
    """使用堆排序对列表进行降序排序。"""
    # 将元素取反后放入最小堆，排序后再取反
    neg_lst = [-x for x in lst]
    heapq.heapify(neg_lst)
    sorted_neg_lst = [heapq.heappop(neg_lst) for _ in range(len(neg_lst))]
    sorted_lst = [-x for x in sorted_neg_lst]
    return sorted_lst

# 示例用法：
if __name__ == "__main__":
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_ascending = heap_sort(unsorted_list.copy())
    print(f"升序排序结果: {sorted_ascending}")

    unsorted_list_desc = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_descending = heap_sort_descending(unsorted_list_desc.copy())
    print(f"降序排序结果: {sorted_descending}")