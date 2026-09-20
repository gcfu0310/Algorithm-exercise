import heapq
class MedianFinder:

    def __init__(self):
        self.data_fluid = []

    def addNum(self, num: int) -> None:
        # heapq.heappush(self.data_fluid,num)
        n = len(self.data_fluid)
        left,right = 0,n
        while left < right:
            mid = (right-left)//2+left
            if self.data_fluid[mid]<num:
                left = mid+1
            else:
                right = mid
        self.data_fluid.insert(right,num)


    def findMedian(self) -> float:
        # n = len(self.data_fluid)
        # if n%2==1:
        #     return self.data_fluid[n//2]
        # else:
        #     return mean(self.data_fluid[n//2-1:n//2+1])
        n = len(self.data_fluid)
        if n%2==1:
            return self.data_fluid[n//2]
        else:
            return mean(self.data_fluid[n//2-1:n//2+1])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

import heapq
class MedianFinder:

    def __init__(self):
        # 大顶堆，用来存放中位数左边的数
        self.max_heap = []
        # 小顶堆，用来存放中位数右边的数
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or -self.max_heap[0]>=num:
            heapq.heappush(self.max_heap,-num)
        else:
            heapq.heappush(self.min_heap,num)
        # 控制两个堆的数量，确保max_heap的数量为min_heap多1或是相等
        if len(self.max_heap) > len(self.min_heap)+1:
            t = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-t)
        if len(self.max_heap) < len(self.min_heap):
            t = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-t)
            
    def findMedian(self) -> float:
        if len(self.min_heap)!=len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0]-self.max_heap[0])/2