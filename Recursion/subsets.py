#https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #print(nums)
        #print(nums)
        if  len(nums)==0:
            return [[]]
        
        ans=self.subsets(nums[1:])
        #print(ans)
        fin=[]
        
        for x in ans:
            temp=[z for z in x]+[nums[0]]
            
            
            
            fin.append(temp)
            
        #print(fin,ans,nums)
        return fin+ans
            
        