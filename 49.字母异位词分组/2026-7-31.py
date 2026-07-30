from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hasnmap = dict()
        ans = list()
        for string in strs:
            # 排序后返回的是list
            sort_string = sorted(string)
            key = ''.join(sort_string)

            if key not in hasnmap:
                hasnmap[key] = [string]
                ans.append(hasnmap[key])
            else:
                hasnmap[key].append(string)
        return ans