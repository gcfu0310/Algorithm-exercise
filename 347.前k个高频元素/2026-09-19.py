class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=1
            else:
                hashmap[nums[i]]+=1
        count = 0
        ans = []
        while count<k:
            max_values = 0
            for key,value in hashmap.items():
                if value > max_values:
                    num = key
                    max_values = value
            ans.append(num)
            count+=1
            del hashmap[num]
        return ans

# 正儿八经的堆写法
# 用的是小顶堆
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=1
            else:
                hashmap[nums[i]]+=1
        heap = []
        for key,value in hashmap.items():
            if len(heap)<k:
                heapq.heappush(heap,(value,key))
            elif value > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap,(value,key))
        return [t[1] for t in heap]
        