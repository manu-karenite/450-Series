#https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==0:
            return [[]]
        
        ans=self.subsetsWithDup(nums[1:])
        sorted_ans=[]
        for z in ans:
            z.sort()
            sorted_ans.append(z)
            
        fin=[]
        for x in ans:
            temp=[z for z in x]+[nums[0]]
            temp.sort()
            
            if temp not in sorted_ans:
                fin.append(temp)
            
        return fin+sorted_ans
        