class BinaryHeap(object):
    def __init__(self):
        self.heap = []

    # 当前节点的父节点就是当前节点的下标减一整除2的结果
    def prec_up(self, i):
        while (i - 1) // 2 >= 0:
            parent_dex = (i - 1) // 2
            if self.heap[parent_dex] > self.heap[i]:
                self.heap[i], self.heap[parent_dex] = self.heap[parent_dex], self.heap[i]
            i = parent_dex

    def insert(self, item):
        self.heap.append(item)
        self.prec_up(len(self.heap) - 1)

    def get_min_chile(self, i):
        """
        索引 i * 2 + 1 通常是索引 i 的左子节点的索引。
        索引 i * 2 + 2 通常是索引 i 的右子节点的索引。
        作用：帮助向下调整操作找到需要与当前节点 i 进行比较和可能交换的子节点。
        :param i: 找到索引为 i 的节点的两个子节点中值较小的那个的索引
        """
        if i * 2 + 1 < len(self.heap) - 1:
            return i * 2 + 1
        if self.heap[i * 2 + 1] < self.heap[i * 2 + 2]:
            return i * 2 + 2
        return i * 2 + 2

    def prec_down(self, i):
        while (i * 2 + 1) < len(self.heap):
            sm_child = self.get_min_chile(i)
            if self.heap[sm_child] < self.heap[i]:
                self.heap[i], self.heap[sm_child] = self.heap[i], self.heap[sm_child]
            else:
                break

            i = sm_child

    def delete(self):
        """
        从二叉堆中删除最小的元素
        :return: 二叉堆中的最小值 即原root值
        """
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        res = self.heap.pop()
        self.prec_down(0)
        return res

    def heapify(self, lst):
        self.heap = lst[:]
        i = len(lst) // 2 - 1  #表示距离叶子节点最近的一个左子树
        while i >= 0:
            self.prec_down(i)
            i = i - 1
































