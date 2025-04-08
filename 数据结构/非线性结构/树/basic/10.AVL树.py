"""
关于AVL树部分从103行开始 前面仍为二叉搜索树的部分 作为实现AVL树的基础
"""


class TreeNode:
    """二叉搜索树的节点"""

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = None
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    """二叉搜索树"""

    def __init__(self):
        self.root = None

    def insert(self, key):
        """插入一个键值到二叉搜索树中"""
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """递归地插入键值"""
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        """搜索二叉搜索树中是否存在给定的键值"""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """递归地搜索键值"""
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def find_min(self):
        """查找树中的最小键值"""
        current = self.root
        while current and current.left is not None:
            current = current.left
        return current.key if current else None

    def find_max(self):
        """查找树中的最大键值"""
        current = self.root
        while current and current.right is not None:
            current = current.right
        return current.key if current else None

    def delete(self, key):
        """从二叉搜索树中删除给定的键值"""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        """递归地删除键值"""
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_right = self._find_min_node(node.right)
                node.key = min_right.key
                node.right = self._delete_recursive(node.right, min_right.key)
        return node

    def _find_min_node(self, node):
        """查找给定节点子树中的最小节点（返回节点对象）"""
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        """中序遍历（返回排序后的键值列表）"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """递归地进行中序遍历"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)


# AVL树实现：


class AVLTreeNode(TreeNode):
    def __init__(self, key, value, balance_factor, left=None, right=None, parent=None):
        self.balance_factor = balance_factor
        super().__init__(key, value, left=None, right=None, parent=None)

    def put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left:
                self.put(key, value, current_node.left)
            else:
                current_node.left = AVLTreeNode(key, value, 0, parent=current_node)
                self.update_balance(current_node.left)

        if key > current_node.key:
            if current_node.right:
                self.put(key, value, current_node.right)
            else:
                current_node.right = AVLTreeNode(key, value, 0, parent=current_node)
                self.update_balance(current_node.right)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return

        if node.parent:
            if node.is_left_child():
                node.parent.balance_factor *= -1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, rotation_root):
        # 定义一个临时变量指向旋转节点的右子树
        new_root = rotation_root.right
        # 将旋转根的右子节点设置为新根的左子节点
        rotation_root.right = new_root.left
        if new_root.left:
            # 如果新根节点有左子节点，则将其父节点设置为旋转根
            new_root.left.parent = rotation_root
        # 为了保持整棵树的平衡  如果有父节点则将新根的父节点设置为旋转根的父节点
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            # 如果旋转根节点是树的根节点，则将新根节点设置为树的根节点
            self.root = new_root
        else:
            # 如果旋转根是他之前父节点的左子树那么新的根节点就会替代他之前的位置，成为他之前父节点的左子树
            # 以上操作（161）原因：为了不影响到非旋转操作的部分的平衡同时维持平衡树的结构平衡
            if rotation_root.is_left_child():
                rotation_root.parent.left = new_root
            else:
                rotation_root.parent.right = new_root

        new_root.left = rotation_root
        rotation_root.parent = new_root
        # + 1: 左旋操作实际上是将 rotation_root 向左下方移动了一层
        rotation_root.balance_factor = rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 - max(rotation_root.balance_factor, 0)

    def rotate_right(self, rotation_root):
        """对以 rotation_root 为根的子树执行右旋操作。"""
        new_root = rotation_root.left  # 将旋转根的左子节点设置为新的根节点
        rotation_root.left = new_root.right  # 将旋转根的左子节点设置为新根节点的右子节点

        if new_root.right:
            new_root.right.parent = rotation_root  # 如果新根节点有右子节点，则将其父节点设置为旋转根节点
        new_root.parent = rotation_root.parent  # 将新根节点的父节点设置为旋转根节点的父节点

        if rotation_root.is_root():
            self.root = new_root  # 如果旋转根节点是树的根节点，则将新根节点设置为树的根节点
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left = new_root  # 如果旋转根节点是其父节点的左子节点，则将新根节点设置为其父节点的左子节点
            else:
                rotation_root.parent.right = new_root  # 如果旋转根节点是其父节点的右子节点，则将新根节点设置为其父节点的右子节点

        new_root.right = rotation_root  # 将旋转根节点设置为新根节点的右子节点
        rotation_root.parent = new_root  # 将新根节点的父节点设置为旋转根节点

        rotation_root.balance_factor = rotation_root.balance_factor - 1 - max(new_root.balance_factor,
                                                                              0)  # 更新旋转根节点的平衡因子
        new_root.balance_factor = new_root.balance_factor - 1 + min(rotation_root.balance_factor, 0)  # 更新新根节点的平衡因子

    def rebalance(self, node):
        # 通过对树的倾斜类型来判断对某个节点进行左旋还是右旋
        if node.balance_factor < 0:
            if node.right.balance_factor > 0:
                self.rotate_right(node.right)
                self.rotate_left(node)
            else:
                self.rotate_left(node)

        elif node.balance_factor > 0:
            if node.left.balance_factor < 0:
                self.rotate_left(node.left)
                self.rotate_right(node)
            else:
                self.rotate_right(node)
