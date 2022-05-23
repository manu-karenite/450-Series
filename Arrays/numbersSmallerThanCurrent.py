#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ans=[]
        for i,x in enumerate(nums):
            target=nums[i]
            
            temp=nums[0:i]+nums[i+1:]
            print(temp)
            ans1=0
            for z in temp:
                if z<target:
                    ans1+=1
            ans.append(ans1)
        return ans
                
        