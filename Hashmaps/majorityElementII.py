# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for x in nums:
            if x in d:
                d[x] = d[x]+1
            else:
                d[x] = 1

        n = len(nums)//3

        lis = []
        for x in d:
            if d[x] > n:
                lis.append(x)
        return lis
