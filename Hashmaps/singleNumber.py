#https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        
        for z in d:
            if d[z]==1:
                return z
        