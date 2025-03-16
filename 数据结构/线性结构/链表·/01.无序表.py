class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return str(self.data)

class UnorderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

# 将新创建的节点 放到链表的最前面

    def add(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp



























































