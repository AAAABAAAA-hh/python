# 将中序表达式 转化为后序表达式
# 例： a * b -> a b *

def mid_t_pos(exs:str) -> str:
    stack = []
    list_map =['1','2','3','4','5','6','7','8','9']
    dict_ope_bra = {'(':0,'[':0,'{':0,'-':1,'+':1,'*':2,'/':2}
    list_ans = []
    list_str = list(exs)
    for ele in list_str:
        if ele in list_map:
            list_ans.append(ele)
        elif ele in ['(','[','{']:
            stack.append(ele)
        elif ele in ')':
            top_taken = stack.pop()
            while top_taken != '(':
                list_ans.append(top_taken)
                top_taken = stack.pop()
        else:
            while not stack and dict_ope_bra[ele] >= dict_ope_bra[stack[-1]]:
                list_ans.append(stack.pop())
            stack.append(ele)

    while not stack:
        list_ans.append(stack.pop())

    return ''.join(list_ans)

# 计算 后序表达式

from pythonds3.basic import *

def math(ope,op1,op2):
    if ope == '+':
        return op1 + op2
    elif ope == '-':
        return op1 - op2
    elif ope == '*':
        return op1 * op2
    elif ope == '/':
        return op1 / op2

def cal_pos(exs:str) -> str:
    ope_stack = Stack()
    list_tok = list(exs)

    for ele in list_tok:
        if ele == '0123456789':
            ope_stack.push(int(ele))
        else:
            ope_1 = ope_stack.pop()
            ope_2 = ope_stack.pop()
            res = math(ele,ope_1,ope_2)
            ope_stack.push(res)

    if ope_stack:
        return ope_stack.pop()
    else:
        return '程序错误 ，栈未被清空。'




























































