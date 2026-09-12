from typing import List
class Solution:
    # 把找中位数的任务转换成找第k小的数
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 第k小(!!不是下标!!)
        def getKth(k:int)->int:
            # 当前两个数组的起始点
            i,j = 0,0
            while True:
                # nums1用完,只能从nums2中取
                if i == len(nums1):
                    return nums2[j+k-1]
                # nums2用完，只能从nums1中取
                if j == len(nums2):
                    return nums1[i+k-1]
                # 当k==1，只用比较两个数组的起始点即可(两个数组都有值，无值的话就从上面跳出去了)
                if k==1:
                    return min(nums1[i],nums2[j])
                # 计算take1和take2，take1和take2计算从两个数组分别拿走几个数
                take1 = min(k//2,len(nums1)-i) # 拿走比较的数目由当前数组中的数目和k//2中较小的那个决定
                take2 = min(k//2,len(nums2)-j)
                # 比较进行筛选
                if nums1[i+take1-1] < nums2[j+take2-1]:
                    # 这种情况说明nums[1]的i~i+take1-1个数都小于nums2[j+take2-1]这个数，那这个范围的数都可以舍去了，它们不可能是第k小的数
                    i += take1 # 更新nums1的起始点
                    k -= take1 # 更新查找的目标
                else:
                    j += take2
                    k -= take2
        total = len(nums1)+len(nums2)
        if total%2==1:
            return getKth(total//2+1) # 奇数情况
        else:
            return (getKth(total//2)+getKth(total//2+1))/2 # 偶数情况