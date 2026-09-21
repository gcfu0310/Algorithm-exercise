# 堆写法(小顶堆)
import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            # 维护长度为k的堆，在长度小于k时，push进堆
            if len(heap)<k:
                heapq.heappush(heap,num)
            else:
                # 当长度等于k时，比较当前这个数和堆顶的数，如果比堆顶的数大，就先pop再push，我们的堆用来存储一共K大的数，第K大的数是其中最小的
                if num >= heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,num)
        return heap[0]