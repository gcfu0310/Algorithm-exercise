from typing import List

class Solution:
    # 时间复杂度为O(nk),空间复杂度为O(1)
    def rotate_1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lun = k // n
        k = k - (lun*n)
        for t in range(k):
            num = nums.pop()
            nums.insert(0,num)


    """翻转数组实现向右移动K的原理解释：
        假设一个数组是nums，长度为n。题目要求向右移动k步，假设nums前n-k个组成切片A，后k个组成切片B，则nums由[A+B]组成。
        现在我们实现向右移动k步，相当与将nums变成[B+A]的形式，所以关键就是计算k值，计算k值之后，直接取切片进行拼接即可。
    """
    # 时间复杂度为O(n),空间复杂度为O(n)
    def rotate_2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]

    """
    方法三和方法二的原理相同，但是空间复杂度降低了，为什么这样子可以降低呢？
    还是和刚才的一样，nums由[A+B]组成，我们的最终目标就是获得[B+A],但是由于方法二是用取切片和拼接的方法，所以切片造成了空间上的负担。
    方法三的流程是这样的：
        1、将整个nums进行翻转，得到：[reversed(B)+reversed(A)]
        2、将reversed(B) and reversed(A)分别再进行一次翻转，即可得到[B+A]
    没有使用切片，就是数组内值的交换，故空间复杂度为O(1)
    """
    # 时间复杂度为O(n),空间复杂度为O(1)
    def rotate_3(self, nums: List[int], k: int) -> None:
        def reverse(left:int,right:int) -> None:
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]

        n = len(nums)
        k = k % n
        # 将数组整个翻转
        reverse(0,n-1)
        # 翻转数组前K个切边
        reverse(0,k-1)
        # 翻转数组后n-k个切片
        reverse(k,n-1)

    # 时间复杂度为O(n),空间复杂度为O(1)
    def rotate_3(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        # 记录已经遍历的元素数
        count = 0
        # 起始点
        start = 0

        # 没遍历完所有数就不结束外层循环
        while count < n :
            # current记录当前遍历的节点
            current = start
            # 保存待交换值
            temp = nums[start]
            while True:
                current = (current+k) % n
                # 记录原current的值
                prev = nums[current]
                # 完成值的交换
                nums[current] = temp
                # 保存待交换的值
                temp = prev
                # 计数加一
                count += 1
                # 如果回到起始点，说明完成一轮循环，更新起始点，并退出内层循环
                if current == start:
                    start += 1
                    break

    
    