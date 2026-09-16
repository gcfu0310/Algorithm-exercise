def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
    ans = [-1]*len(nums1)
    hashmap = {}
    stack = list()
    # 构造哈希映射表 时间复杂度：O(n)
    for i in range(len(nums1)):
        hashmap[nums1[i]] = i
    # 遍历数组nums2 时间复杂度：O(m)
    for j in range(len(nums2)):
        # 栈非空且当前的数比入栈的数大，说明找到比当前这个nums1[stack[-1]]下一个更大的数nums2[j]
        while stack and nums2[j]>nums1[stack[-1]]:
            # 把下标弹出
            idx=stack.pop()
            # 赋值
            ans[idx] = nums2[j]
        # 当前数是nums1中的数，将该数在nums1中对应的下标入栈
        if nums2[j] in hashmap:
            stack.append(hashmap[nums2[j]])
    return ans