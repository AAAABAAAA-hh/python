 #本例将前序 中序  后序 都实现为外部函数
import operator
from linecache import cache


def preorder(tree):
    # 前序
    if tree is None:
        return False
    else:
        print(tree)
        preorder(tree.left_child)
        preorder(tree.right_child)

def inorder(tree):
    # 中序
    if tree is None:
        return False
    else:
        inorder(tree.left_child)
        print(tree)
        inorder(tree.right_child)

def postorder(tree):
    # 后序
    if tree is None:
        return False
    else:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree)

#应用后序重写计算函数
def posordereval(tree):
    operators = {
        "+": operator.add ,
        "-": operator.sub ,
        "*": operator.mul ,
        "/": operator.truediv,
    }

    if tree is None:
        return False
    else:
        res_1 = posordereval(tree.left_child)
        res_2 = posordereval(tree.right_child)
        if res_1 and res_2:
            return operators[tree.key](res_1, res_2)
        return tree.key

#中序还原表达式
def  print_exp(tree):
    res = ""
    if tree is not None:
        res = res + "(" + print_exp(tree.left_child)
        res = res + str(tree.key)
        res = (res + print_exp(tree.right_child) + ")")

    return res























