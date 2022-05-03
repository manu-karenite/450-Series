#https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d={}
        for x in nums:
            if x in d:
                d[x]=d[x]+1
            else:
                d[x]=1
        
        for y in d:
            if d[y]%2==1:
                return False
        return True
        