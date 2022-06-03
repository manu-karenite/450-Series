#https://leetcode.com/problems/maximum-subarray/submissions/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far=-2**31
        max_end_here=0
        
        for x in nums:
            max_end_here+=x
            if max_so_far<max_end_here:
                max_so_far=max_end_here
            if max_end_here<0:
                max_end_here=0
        return max_so_far
        