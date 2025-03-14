# 实现传土豆          计数常量为 7

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self,element):
        self.q.append(element)

    def dequeue(self):
        return self.q.pop(0)

    def size(self):
        return len(self.q)

    def is_empty(self):
        return not self.q

def hot_potato(list_mem,num):
    sim_queue = Queue()
    for i in range(len(list_mem)):
        sim_queue.enqueue(list_mem[i])

    while sim_queue.size() > 1:             #保证队列在最后一次取 ans 时队列不为空 否则会报错 也可以取消最后的pop操作 将size变为 》0 但是需要一个变量接收while循环后的ans 来作为函数的返回值
        for i in range(len(sim_queue.q)):
            ele = sim_queue.dequeue()
            sim_queue.enqueue(ele)
        sim_queue.dequeue()

    return sim_queue.dequeue()  #执行完此行代码后 队列为空

list_num = list(map(str,input("请输入有限个名称：").split()))
hot_potato(list_num,len(list_num))
# ans
print(hot_potato(list_num,len(list_num)))
























