#https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=str("")
        for x in nums:
            ans=ans+str(x)
        
        oneList=ans.split("0")
        print(oneList)
        
        maxLimit=-1
        
        for x in oneList:
            curr=len(x)
            if curr>maxLimit:
                maxLimit=curr
            
        return maxLimit
            