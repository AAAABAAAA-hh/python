#  实现 基础队列 数据类型
class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self,element):
        self.q.insert(0, element)

    def dequeue(self):
        self.q.pop()

    def size(self):
        return len(self.q)

    def is_empty(self):
        return not self.q










































