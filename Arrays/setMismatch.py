#https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        found=set()
        n=len(nums)
        ans=-1
        for x in nums:
            if x in found:
                ans=x
            else:
                found.add(x)
                
        ans2=int((n*(n+1))/2)
        z=0
        for y in found:
            z=z+y
        print(ans2,z)   
        return [ans,ans2-z]
            
        