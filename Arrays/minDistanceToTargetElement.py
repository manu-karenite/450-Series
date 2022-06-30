#https://leetcode.com/problems/minimum-distance-to-the-target-element/

from math import fabs
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        idx=[]
        for i,x in enumerate(nums):
            if x==target:
                idx.append(i)
                
        m=2**31-1
        for x in idx:
            m=min(int(fabs(x-start)),m)
        return m
        