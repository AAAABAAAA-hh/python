from pythonds3.basic import *

def turn_str(num, base):
    r_stack = Stack()
    map_tab = "0123456789ABCDEFG"
    while num > 0:
        if num < base:
            r_stack.push(map_tab[num])
            break
        else:
            r_stack.push(map_tab[num % base])
            num = num // base
    ans = ""

    while not r_stack.is_empty():
        ans += r_stack.pop()
    return ans

# 测试
print(turn_str(23112,16))











