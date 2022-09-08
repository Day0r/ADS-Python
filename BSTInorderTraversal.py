from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]):
    for i in range(0, len(root), 3):
        print(i)

root = [1,None,2,3]
inorderTraversal(root)