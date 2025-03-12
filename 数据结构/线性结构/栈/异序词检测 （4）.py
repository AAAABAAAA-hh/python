"""
    异序词检测算法: 以下算法时间复杂度由慢到快
    但是不考虑空间复杂度 往往时间越快 占用内存越多
"""

#一 : 暴力法：穷举所有可能 此方案较为复杂 时间复杂度为 n的阶乘 在此不进行示例

# print("较为复杂，不再演示")

#二： 清点法：将其中一个字符串中的字符与另一个字符串中的字符一一对应  n ** 2

def check_str(s1: str, s2: str) -> bool:
    ans = True
    if len(s1) != len(s2):
        ans = False
    list_check = list(s2)
    pos = 0
    while pos < len(s1):
        pos_2 = 0
        found = False
        while pos_2 < len(list_check) and found :
            if list_check[pos_2] == s1[pos]:
                found = True
                break
            else:
                pos_2 += 1
        if found:
            list_check[pos_2] = None
        else:
            ans = False
        pos += 1

    return ans

#三：排序比较法 将字符串化为列表，运用sort方法将二十六个字母排序，一一对应
#sort 方法排序 时间复杂度为 n ** 2 \ nlogn

def chk_str(s1: str, s2: str) -> bool:
    list_chk_1 = list(s1)
    list_chk_2 = list(s2)
    pos = 0
    ans = True
    list_chk_1.sort(reverse = False)
    list_chk_2.sort(reverse = False)
    while pos < len(list_chk_1) and ans:
        if list_chk_1[pos] == list_chk_2[pos]:
            pos += 1
        else:
            ans = False

    return ans

# 四：计数比较法 ：巧妙利用 ord()函数将字母字符转为asc码值
#利用差值所在位置的个数来确定两个字符串的各个字符的个数——》只要差值个数相等就说明两个字符串的构成的字符的种类和个数相同
def check_string(s1: str, s2: str) -> bool:
    list_1 = [] * 26
    list_2 = [] * 26
    for i in range(len(s1)):
         pos = ord(s1[i]) - ord('a')
         list_1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        list_1[pos] += 1
    j = 0
    ans = True
    while j < 26 and ans:
        if list_1[j] == list_2[j]:
            j = j + 1
        else:
            ans = False

    return ans




























































