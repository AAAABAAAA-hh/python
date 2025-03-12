"""
    check '(' ')'
    经过修改可以接受任何字符串，不再局限于只包含括号的字符串
"""

#此为 基础括号匹配
# def par_checker(string):
#     stack = []
#     for char in string:
#         if char == '(' :
#             stack.append(char)
#         elif char == ')' :
#             if not stack:
#                 return False
#             else:
#                 stack.pop()
#         else:
#             pass
#     return not stack

# 此为 全括号匹配 通用
def check_all(s1: str) ->bool :
    stack  = []
    for char in s1:
        if char in ['(','{','['] :
            stack.append(char)
        elif char in ['(','{','[']:
            if  not bool(stack):
                return False
            else:
                a = stack.pop()
                if  not match(char,a):
                    return False
        else:
            pass
        return bool(stack)

def match(left,right) ->bool :
    list_1 = ['(','{','[']
    list_2 = [')','}',']']
    return list_1.index(left) == list_2.index(right)






























