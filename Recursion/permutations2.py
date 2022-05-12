#https://leetcode.com/problems/permutations-ii/

class Solution:
    
    def getAns(self,nums):
        
        if len(nums)==1:
            return [nums]
        
        #otherwise, get from one next to it
        temp=nums[1:]

        ans=self.getAns(temp)

        ret=[]
        s=set()
        for x in ans:
            #mutation not allowed
            
            for i in range(0,len(x)+1):
                p=[]
                for z in x:
                    p.append(z)
                #print(p,i)
                p.insert(i,nums[0]) 
                #print("after",p)
                if p not in ret:
                    
                    ret.append(p)
        
        return ret
                
        
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=self.getAns(nums)
        return ans
        