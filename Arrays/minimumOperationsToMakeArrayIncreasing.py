#https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        
        ct=0
        for i in range(1,len(nums)):
            curr=nums[i]
            prev=nums[i-1]
            print(prev,curr)
            if prev<curr:
                ct+=0
                
            else:
                target=prev+1
                ct+=target-curr
                nums[i]=target
        print(nums)
        return(ct)
        