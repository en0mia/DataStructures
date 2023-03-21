# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 21/03/23
from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root: TreeNode, value) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(value)

    if value < root.val:
        root.left = insert(root.left, value)
    elif value > root.val:
        root.right = insert(root.right, value)
    # Do not insert if the element already exists
    return root


def search(root: TreeNode, value):
    if root is None:
        return False

    if value > root.val:
        return search(root.right, value)
    elif value < root.val:
        return search(root.left, value)
    return True
