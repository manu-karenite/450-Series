#https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        t=[]
        for x in nums:
            t.append(x)
        nums.sort()
        
        larg=nums[-1]
        print(nums,larg)
        i=0
        while i<len(nums)-1:
            curr=nums[i]
            print(curr)
            if curr*2>larg:
                return -1
            
            i=i+1
        return t.index(larg)
                