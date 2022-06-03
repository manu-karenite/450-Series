#https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        
        ans=[]
        print(d)
        for z in d:
            if d[z]==1:
                ans.append(z)
        return ans
        