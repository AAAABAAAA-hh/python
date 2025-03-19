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


class LinkStack:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length

    def peek(self):
        return self.head.getdata()

    def push(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp
        self.length += 1
        
    def pop(self):
        del_date = self.head.getdata()
        self.head = self.head.next
        self.length -= 1
        return del_date

























