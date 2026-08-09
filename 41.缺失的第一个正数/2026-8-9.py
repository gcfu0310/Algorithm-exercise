from typing import List

class Solution:
    # 时间复杂度为O(n),空间复杂度为O(n)
    def firstMissingPositive_1(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        Flag = True
        min_num = 0
        for i in range(n):
            if Flag and nums[i] > 0:
                min_num = nums[i]
                Flag = False
            if nums[i] <= 0:
                continue
            if nums[i] < min_num:
                min_num = nums[i]
            s.add(nums[i])
        
        if min_num != 1:
            return 1
        while True:
            if min_num + 1 not in s:
                return min_num + 1
            min_num += 1

    # 时间复杂度为O(n),空间复杂度为O(1)
    """
    这道题目要求找到数组中缺失的第一个正数，也就是最小的正数。一个长度为n的数组，其中没出现的最下正数只有可能出现在[1,n+1]
    我们只用把现有的数按照1~n+1的顺序重新排列到数组中，然后从第一个数向右遍历，不满足nums[i] == i+1的数，就是缺失的最小正数
    """
    def firstMissingPositive_2(self, nums: List[int]) -> int:
        n = len(nums)
        # 遍历数组中的每一个数
        for i in range(n):
            # 如果当前这个数在[1,n]这个范围，而且和待交换区域的数不相等时，就发生交换
            while 1<=nums[i]<=n and nums[i] != nums[nums[i]-1]:
                # 计算出待交换的下标
                j = nums[i]-1
                # 交换两个数
                nums[i],nums[j] = nums[j],nums[i]
        # 现在的数组已经是按照1~n的顺序排列的
        for i in range(n):
            # 找到下标和值无对应关系，就返回下标+1
            if nums[i] !=  i+1:
                return i+1
        return n+1

    # 时间复杂度为O(n),空间复杂度为O(1) 缺点在于会损坏数组原本的值
    """
    总体上和方法二的思路是一致的，方法三属于是标记法，原理是这样的：
    1、把数组中所有非正值赋值成n+1
    2、数组中值为num（小于等于n），把它对应下标的值赋值成负的，表示该下标的值是存在的
    3、再重新遍历一遍数组，当检测到值为正时，说明这个下标对应的就是缺失的最小正数
    """
    def firstMissingPositive_3(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num-1] = -abs(nums[num-1]) # 右边的abs一定要加，防止出现重复的情况，比如说：[1,1]
        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        return n+1