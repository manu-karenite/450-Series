# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = set(nums)
        for x in nums:
            if x in a:
                a.remove(x)
            else:
                return x
