#https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        s=set()
        for x in nums:
            if x in s:
                ans.append(x)
            s.add(x)
        return ans
            
        
        