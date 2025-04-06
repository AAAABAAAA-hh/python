
class BinaryTree:
    left_child = None
    right_child = None
    key = None
    def __iter__(self, ):
        if self:
            if self.left_child:
                for elem in self.left_child:
                    yield elem

            yield self.key

            if self.right_child:
                for elem in self.right_child:
                    yield elem

















