#https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        result = inc = dec = 1
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc  = dec + 1
            elif nums[i] > nums[i+1]:
                dec = inc + 1
            result = max(result,max(inc,dec))
        return result