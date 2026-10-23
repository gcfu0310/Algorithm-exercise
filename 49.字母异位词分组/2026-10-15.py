import collections
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hasnmap = collections.defaultdict(list)
        for s in strs:
            counts = [0]*26
            for ch in s:
                counts[ord(ch)-ord('a')]+=1
            hasnmap[tuple(counts)].append(s)
        return list(hasnmap.values())
    
        
        