# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 递归
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []

        self.loop(root)
        return self.ans

    def loop(self,root):
        if root == None:
            return 
        self.loop(root.left)
        self.ans.append(root.val)
        self.loop(root.right)