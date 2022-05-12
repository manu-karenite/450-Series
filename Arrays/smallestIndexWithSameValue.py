#https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for idx,item in enumerate(nums):
            if idx%10==item:
                return idx
        return -1
        