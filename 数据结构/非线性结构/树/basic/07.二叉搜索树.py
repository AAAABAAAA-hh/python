
"""                     AI                    """
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

    def is_empty(self):
        return self.root is None

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
        # 如果 key == node.key，通常我们不插入重复的值，这里选择忽略

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

    def find_min(self, node=None):
        """查找以给定节点为根的子树中的最小键值"""
        if node is None:
            node = self.root
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.key

    def find_max(self, node=None):
        """查找以给定节点为根的子树中的最大键值"""
        if node is None:
            node = self.root
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.key

    def delete(self, key):
        """从二叉搜索树中删除给定的键值"""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        """递归地删除键值"""
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:  # 找到要删除的节点
            # 情况 1: 叶子节点或只有一个子节点
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 情况 2: 有两个子节点
            # 找到右子树中的最小节点（也可以选择左子树中的最大节点）
            min_right = self._find_min_node(node.right)
            # 将要删除节点的值替换为右子树最小节点的值
            node.key = min_right.key
            # 在右子树中删除这个最小节点
            node.right = self._delete_recursive(node.right, min_right.key)
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

    def preorder_traversal(self):
        """先序遍历"""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        """递归地进行先序遍历"""
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        """后序遍历"""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        """递归地进行后序遍历"""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)

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

    print("中序遍历 (排序后):", bst.inorder_traversal()) 
    print("先序遍历:", bst.preorder_traversal())
    print("后序遍历:", bst.postorder_traversal())

    print("查找 40:", bst.search(40).key if bst.search(40) else "未找到")
    print("查找 90:", bst.search(90).key if bst.search(90) else "未找到")

    print("最小值:", bst.find_min())
    print("最大值:", bst.find_max())

    bst.delete(30)
    print("删除 30 后的中序遍历:", bst.inorder_traversal())

    bst.delete(70)
    print("删除 70 后的中序遍历:", bst.inorder_traversal())































