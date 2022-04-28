#https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,2*len(nums)):
            ans.append(0)
        for i  in range(0,len(nums)):
            ans[i]=nums[i]
            ans[i+len(nums)]=nums[i]
        
        return ans
        
        