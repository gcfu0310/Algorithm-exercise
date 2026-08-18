from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 时间复杂度是O(n),空间复杂度是O(n)+O(h)=O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = list()
        def loop(root:Optional[TreeNode]):
            if root is None:
                return 
            loop(root.left)
            ans.append(root.val)
            loop(root.right)
        loop(root)
        return ans[k-1]

    def kthSmallest_1(self, root: Optional[TreeNode], k: int) -> int:
        t = 0
        ans = 0
        def loop(root:Optional[TreeNode]):
            nonlocal t,ans
            # 遍历导空值时
            if root is None:
                return 
            loop(root.left)
            # 检查左子树中是否找到了第k小的数，找到就return
            if t == k:
                return 
            t += 1
            # 找到之后return，在这个loop中结束，不代表在外层就结束，所以一定要在前面加一个
            if t == k:
                ans = root.val
                return 
            # 即使右子树找到了答案，回来以后当前层也已经走到函数末尾，自然结束，所以不需要再写
            # 递归调用返回后，如果后面还有可能“不该再执行”的代码，就要检查是否已经满足终止条件。
            loop(root.right)
        loop(root)
        return ans
"""
loop(5)
   ↓ 调用
loop(3)
   ↓ 调用
loop(2)
"""
