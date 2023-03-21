# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 21/03/23
from typing import Optional


class TreeNode:
    def __init__(self, val: Optional[str], is_termination=False, is_root=False):
        self.is_root = is_root
        self.is_termination = is_termination
        self.val = val
        self.children = {}


def dfs(root: TreeNode, prefix: str, results: list) -> None:
    if root.is_termination:
        results.append(prefix)

    for child in root.children.values():
        dfs(child, prefix + child.val, results)


def insert(root: Optional[TreeNode], val: str) -> TreeNode:
    if root is None:
        root = TreeNode(None, False, True)
        return insert(root, val)
    current = root

    for c in val:
        if c in current.children:
            current = current.children[c]
        else:
            current.children[c] = TreeNode(c)
            current = current.children[c]

    current.is_termination = True
    return root


def is_prefix(root: TreeNode, val: str) -> bool:
    current = root

    for c in val:
        if c not in current.children:
            return False
        current = current.children[c]
    return True


def get_words(root: TreeNode, prefix: str) -> list:
    current = root

    for c in prefix:
        if c not in current.children:
            return []
        current = current.children[c]

    results = []
    dfs(current, prefix, results)

    return results
