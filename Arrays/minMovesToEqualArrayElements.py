#https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

from math import fabs
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()


        term=nums[len(nums)//2]
        s=0
        for x in nums:
            s+=int(fabs(x-term))
        return s
        