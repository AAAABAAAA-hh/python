from asyncio import current_task


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

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next
        if current is None:
            raise ValueError("item not a list")

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def search(self,item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    # 关于 append insert index pop 练习
    def append(self,item):
        current = self.head
        app_node = Node(item)
        while current is not None:
            if current.next is None:
                current.next = app_node

    def insert(self, position, item):
        if position < 0:
            print("位置无效")
            return

        new_node = Node(item)
        # 在头部插入
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for i in range(position - 1):
            if current is None:
                print("位置超出链表长度")
                return
            current = current.next

        if current is None:
            print("位置超出链表长度")
            return

        new_node.next = current.next
        current.next = new_node
"""
    剩下两种方法基本与 insert相同步 不再 赘述 
    写出 链表 的各种 操作 主要是要注意 各个 引用所对应的指向 注意 特殊位置 的 特殊处理
"""




















































