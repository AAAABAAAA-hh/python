
#以列表的最后一个元素作为栈顶
class Stack1:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return  not bool(self.stack)
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)

#以列表得第一个元素处作为栈顶
class Stack2:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not bool(self.stack)

    def push(self, data):
        self.stack.insert(0,data)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

#引用外置库来实现栈
from pythonds3.basic import *
stack = Stack()















