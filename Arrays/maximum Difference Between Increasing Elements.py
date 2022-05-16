# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        result = -1
        min_so_far = nums[0]

        for i in range(1, len(nums)):
            result = max(result, nums[i] - min_so_far)
            min_so_far = min(min_so_far, nums[i])

        if result == 0:
            return -1
        else:
            return result
