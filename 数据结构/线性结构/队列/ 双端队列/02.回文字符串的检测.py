# 回文序列的检测
from time import time
from pythonds3.basic import Deque

f_time = None

def check_pal(test: str) -> bool:
    global f_time
    st_time = time()
    chk_deque = Deque()

    if type(test) == int:
        test = str(test)

    for item in test:
        chk_deque.add_front(item)

    while chk_deque.size() > 1:
        first = chk_deque.remove_front()
        second = chk_deque.remove_rear()

        if first != second:
            return False

    lt_time = time()
    f_time = lt_time - st_time
    print(f_time)
    return True

print(check_pal("13131"))








