
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

class LinkQueue(object):
    def __init__(self):
        """
        head: 链表头作为队列的头
        tail：链表尾作为队列的尾
        """
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def enqueue(self,date):
        temp = Node(date)
        if self.head is None:
            self.head = temp
        else:
            self.tail.set_next(temp)
            self.tail = self.tail.get_next()
            self.length += 1

    def dequeue(self):
        pop_date = self.head.get_data()
        if self.head is self.tail:
            self.head =  self.tail = None
        else:
            self.head = self.head.get_next()
            self.length -= 1

        return pop_date

    def size(self):
        return self.length






