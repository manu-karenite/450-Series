#https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0 or k%len(nums)==0:
            return nums
        l=len(nums)
        k=k%l
        print(k)
        print(l-k)
        orig=nums[l-k:]+nums[:l-k]
        for i in range(0,l):
            nums[i]=orig[i]
        
        