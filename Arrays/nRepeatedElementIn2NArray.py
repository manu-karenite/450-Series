# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            if x in dic:
                dic[x] = dic[x]+1
            else:
                dic[x] = 1

        for y in dic:
            if dic[y] == (len(nums)//2):
                return y
