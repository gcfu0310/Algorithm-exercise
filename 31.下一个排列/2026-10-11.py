class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        字典序:比较两个排列时，从左往右逐位比较，遇到第一个不同的数字，数字较大的那个排列就更大。
        下一个排列不是随便找一个更大的排列，而是要找紧挨着当前排列的那个,比当前排列大的最小排列
        越靠左的数字对排列大小的影响越大,因此要想尽可能小的增大当前这个排列,应该从右开始找起
        如果一段是降序的排列,说明此时已经是最大排列了,因此需要找第一个升序排列的位置,即pivot
        找到pivot之后,把pivot和pivot右边大于pivot的最小数进行交换,就完成了排列变大的第一步
        根据字典序的定义可知,完成以上步骤后,新排列已经大于旧排列,但此时新排列并非最小
        实现最小很简单,把pivot右边变成升序即可
        """
        n = len(nums)
        # 枢轴pivot
        pivot = -1
        if n>=2:
            i = n-2
            # 从右往左找
            while i>=0:
                # 找到第一个升序部分
                if nums[i]<nums[i+1]:
                    # 记录枢轴位置
                    pivot = i
                    j=n-1
                    # 找到枢轴右边比枢轴大的最小数
                    while j>pivot:
                        if nums[j]>nums[pivot]:
                            nums[j],nums[pivot]=nums[pivot],nums[j]
                            break
                        j-=1
                    break
                i-=1
        # 把枢轴右边变成升序。由于枢轴右边是降序的，所以只需使用翻转，即可实现升序
        left = pivot+1
        right = n-1
        while left<right:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
            right-=1
        