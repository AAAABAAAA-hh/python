# 十进制转二进制  利用栈的反转特性
def ten_turn_two(n: int) -> int | str:
    stack = []
    if n == 0:
        return 0
    else:
        while n > 0:
            x = n % 2
            stack.append(x)
            n = n // 2
    return str(stack[::-1])

# 测试1
print(ten_turn_two(10))

#若想转换为任意进制 需要添加一个映射表，通过映射表的查找来进行余数的表示





















