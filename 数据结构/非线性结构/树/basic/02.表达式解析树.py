from pythonds3.basic import Stack
from pythonds3.trees import BinaryTree
import string

def build_parse_tree(fpexp):
    """
    构建表达式解析树。

    Args:
        fpexp: 包含完整括号的算术表达式字符串。

    Returns:
        一个 BinaryTree 对象，表示表达式的解析树。

    current_tree: 用于调用对每个树的引用 注意观察本引用的指向

    """
    pStack = Stack()
    tree = BinaryTree('')
    pStack.push(tree)
    current_Tree = tree
    for token in fpexp:
        if token == '(':
            # 遇到左括号，创建新的左子节点，并将当前节点移到左子节点
            current_tree.insertLeft('')
            pStack.push(current_tree)
            current_tree = current_tree.getLeftChild()
        elif token in ['+', '-', '*', '/']:
            # 遇到操作符，将操作符设置为当前节点的值，并创建空的右子节点
            current_tree.setRootVal(token)
            current_tree.insertRight('')
            pStack.push(current_tree)
            current_tree = current_tree.getRightChild()
        elif token == ')':
            # 遇到右括号，表示当前子表达式结束，返回到父节点
            current_tree = pStack.pop()
        elif token in string.digits:
            # 遇到数字，将其设置为当前节点的值，并返回到父节点
            current_tree.setRootVal(int(token))
            parent = pStack.pop()
            current_tree = parent
        elif len(token) > 1 and token.isdigit():
            # 处理多位数字
            current_tree.setRootVal(int(token))
            parent = pStack.pop()
            current_tree = parent

    return tree
























