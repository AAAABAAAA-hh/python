#进行进制转换 注意 将结果倒序

def turn_str(num,base):
    map_tab = "0123456789ABCDEFG"
    if num < base:
        return map_tab[num]
    else:
        return map_tab[num % base] + turn_str(num // base, base)














