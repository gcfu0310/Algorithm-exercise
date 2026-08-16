from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 时间复杂度是O(n),空间复杂度是O(logn+n)，也就是O(n)
    # 创建nums[0,mid]和nums[mid+1,n]，属于是额外占用了O(n)的空间
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None
        mid = n // 2
        root = TreeNode(val=nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:n])
        return root

    # 时间复杂度是O(n),空间复杂度是O(logn)
    # 采用作为记录左右边界，而不是直接取整个数组
    def sortedArrayToBST_2(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left:int,right:int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left+right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left,mid-1)
            root.right = helper(mid+1,right)
            return root

        return helper(0,len(nums)-1)