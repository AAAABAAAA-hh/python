
"""                 AI                """

from functools import cache

class TreeNode:
    """二叉搜索树的节点"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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

    def delete(self, key):
        """从二叉搜索树中删除给定的键值"""
        self.root = self._delete_recursive(self.root, key)
    @cache
    def _delete_recursive(self, node, key):
        """递归地删除键值，并处理三种情况"""
        if node is None:
            return None  # 未找到要删除的节点

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:  # 找到要删除的节点

            # 情况 1: 要删除的节点是叶子节点（没有子节点）
            if node.left is None and node.right is None:
                return None

            # 情况 2: 要删除的节点只有一个子节点
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 情况 3: 要删除的节点有两个子节点
            else:
                # 找到右子树中的最小节点（作为后继节点）
                successor = self._find_min_node(node.right)
                # 将要删除节点的值替换为后继节点的值
                node.key = successor.key
                # 在右子树中递归删除后继节点（此时后继节点必然是情况 1 或情况 2）
                node.right = self._delete_recursive(node.right, successor.key)
        return node

    def _find_min_node(self, node):
        """查找给定节点子树中的最小节点（返回节点对象）"""
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        """中序遍历（结果是排序后的键值列表）"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """递归地进行中序遍历"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

# 示例用法
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("初始中序遍历:", bst.inorder_traversal())

    # 删除叶子节点 (20)
    bst.delete(20)
    print("删除 20 后的中序遍历:", bst.inorder_traversal())

    # 删除只有一个子节点的节点 (30)
    bst.delete(30)
    print("删除 30 后的中序遍历:", bst.inorder_traversal())

    # 删除有两个子节点的节点 (50)
    bst.delete(50)
    print("删除 50 后的中序遍历:", bst.inorder_traversal())

    # 删除不存在的节点
    bst.delete(90)
    print("尝试删除 90 后的中序遍历:", bst.inorder_traversal())






























