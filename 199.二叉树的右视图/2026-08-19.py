# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional,List

class Solution:
    # 时间复杂度是O(n),空间复杂度是O(w),w是树的最宽层
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        ans = []
        while queue:
            l = len(queue) # 每层的宽度
            ans.append(queue[-1].val)
            for _ in range(l):
                node = queue.popleft() # 用deque的原因，popleft的时间复杂度是O(1)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return ans

        