#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        l=nums[-2]
        r=nums[-1]
        return ((l-1)*(r-1))
        