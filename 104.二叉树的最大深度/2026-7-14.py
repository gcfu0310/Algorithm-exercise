# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root == None:
            return depth
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth,right_depth) + 1
    
class Solution:
    def maxDepth(self,root:Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            next_level = []
            for node in queue:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            queue = next_level
        return depth 