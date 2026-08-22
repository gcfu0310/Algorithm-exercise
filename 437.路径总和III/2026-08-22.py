# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 时间复杂度是O(n^2),空间复杂度是O(h)
    def pathSum_1(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def countPathSum(root,targetSum):
            nonlocal count
            if root is None:
                return 
            if root.val == targetSum:
                count += 1
            countPathSum(root.left,targetSum-root.val)
            countPathSum(root.right,targetSum-root.val)
        
        def helper(root,targetSum):
            if root is None:
                return None
            countPathSum(root,targetSum)
            helper(root.left,targetSum)
            helper(root.right,targetSum)
        
        helper(root,targetSum)
        return count

    # 时间复杂度是O(n),空间复杂度是O(h)
    def pathSum_2(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        prefix_count = {0:1}
        def dfs(root, current_sum):
            nonlocal count,prefix_count
            if root is None:
                return

            current_sum += root.val

            need = current_sum - targetSum
            count += prefix_count.get(need, 0)

            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

            dfs(root.left, current_sum)
            dfs(root.right, current_sum)

            prefix_count[current_sum] -= 1

        dfs(root,0)
        return count


        