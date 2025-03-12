import random
from pythonds3.basic import *

class Printer(object):
    def __init__(self,ppm):
        """
        此代表打印机类
        :param ppm: 表示设置的打印机的打印速率 以分为单位
        """
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def is_empty(self):
        return self.current_task is None

    def tick(self):
        if self.is_empty():
            self.time_remaining = self.time_remaining - 1
        if self.time_remaining <= 0:
            self.current_task = None

    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

class Task(object):
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randint(1,21)

    def get_pages(self):
        return self.pages

    def get_stamp(self):
        return self.timestamp

    def wait_time(self, current_time):
        return current_time - self.timestamp

def new_print_task():
    num = random.randint(1,181)
    return num == 99

def simlation(num_seconds,page_per_minute):
    printer = Printer(page_per_minute)
    print_queue = Queue()
    waiting_time = []

    for i in range(num_seconds):
        if new_print_task():
            task = Task(i)
            print_queue.enqueue(task)

        if not printer.is_empty() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_time.append(next_task.wait_time(i))
            printer.start_next(next_task)

    if not waiting_time:  # 检查 waiting_time 列表是否为空
        return f"No tasks waited, {print_queue.size():3d} tasks remaining."
    else:
        average_time = sum(waiting_time) / len(waiting_time)
        return f"Average Wait {average_time:.2f} secs, {print_queue.size():3d} tasks remaining."



# 测试案例
for i in range(10):
    ans = simlation(1000,1)
    print(ans)



















