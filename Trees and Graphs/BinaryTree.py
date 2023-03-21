# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 21/03/23

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Note: this is particularly important when used with a BST, because it allows to traverse the tree in ascending
# order
def in_order_traversal(root: TreeNode) -> None:
    if root is None:
        return
    in_order_traversal(root.left)
    print(root.val)
    in_order_traversal(root.right)


def pre_order_traversal(root: TreeNode) -> None:
    if root is None:
        return
    print(root.val)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


def post_order_traversal(root: TreeNode) -> None:
    if root is None:
        return
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.val)
