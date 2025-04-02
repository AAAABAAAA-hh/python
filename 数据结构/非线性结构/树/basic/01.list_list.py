"""
    通过 列表与列表的方式构建 树
    示例  二叉树 binary_tree = ["a",["b",[],[]],["c",[],[]]]
    其中 a 为 root  一般认为 b处的位置为 左子树  c处即为 右子树
"""



def make_binary_tree(root):
    return [root,[],[]]

# test
binary_tree = make_binary_tree("a")

def get_root_val():
    return binary_tree[0]

def set_root_val(val):
    binary_tree[0] = val

def get_left_child():
    return binary_tree[1]

def set_left_child(val):
    binary_tree[1] = val

def get_right_child():
    return binary_tree[2]

def set_right_child(val):
    binary_tree[2] = val

def insert_tree_left(new_tree):
    if len(binary_tree[1]) == 1:
        binary_tree[1].insert(1, new_tree)

    else:
        binary_tree[1].append(new_tree)
































