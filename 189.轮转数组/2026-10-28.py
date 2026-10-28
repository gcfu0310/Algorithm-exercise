class Solution:
    def rotate_1(self, nums: list[int], k: int) -> None:
        # 时间复杂度为O(n),空间复杂度为O(1)
        # 模拟数组轮转的过程
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # start是开始移动数的下标，count是指已有多少数完成了移动
        start,count=0,0
        # 当count=n时移动完成
        while count<n:
            # 记录开始的下标和值
            current_index=start
            current_value=nums[current_index]

            while True:
                # 计算当前移动终点的下标并保存终点下标的值
                next_index=(current_index+k)%n
                next_value=nums[next_index]
                # 完成移动
                nums[next_index]=current_value
                # 更新下一个移动的下标和对应值
                current_index=next_index
                current_value=next_value
                # 记录加一
                count+=1
                # 如果移动后当前的下标等于一开始的start，说明已经完成了start开始一轮的移动
                if current_index==start:
                    # 更新start
                    start+=1
                    break
    
    def rotate_2(self, nums: list[int], k: int) -> None:
        # 时间复杂度为O(n),空间复杂度为O(n)
        # nums=[A+B],len(A)=n-k,len(B)=k, nums finishes rotation to [B+A]
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        A=nums[:n-k]
        B=nums[n-k:]
        nums[:]=B+A

    # 时间复杂度为O(n),空间复杂度为O(1)
    def rotate_3(self, nums: list[int], k: int) -> None:
        # 与方法二类似，先做一次整体数组的左右翻转，nums=[reversed(B)+reversed(A)],再接着对reversed(B)和reversed(A)做一次翻转，最后变成[B+A]
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        n=len(nums)
        k%=n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)