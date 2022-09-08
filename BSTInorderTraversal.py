from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]):
    result = []
    recHelper(root, result)
    return result


def recHelper(root, result):
    if root:
        recHelper(root.left, result)
        result.append(root.val)
        recHelper(root.right, result)
