# 通过类 的性质来构建树
class BinaryTreeNode(object):
    def __init__(self, root_data):
        self.key = root_data
        self.left_child = None
        self.right_child = None

    def insert_left(self,new_date):
        #从树的根部插入
        if self.left_child is None:
            self.left_child = BinaryTreeNode(new_date)
        else:
            new_node = BinaryTreeNode(new_date)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, new_date):
        # 插入位置和左子树相同
        if self.right_child is None:
            self.right_child = BinaryTreeNode(new_date)
        else:
            new_node = BinaryTreeNode(new_date)
            new_node.right_child = self.right_child
            self.right_child = new_node

    # 关于二叉树的 访问函数不在赘述
    # 二叉树的 所有子树都为二叉树
    



































