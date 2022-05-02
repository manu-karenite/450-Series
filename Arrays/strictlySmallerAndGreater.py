#https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/submissions/

class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        count=0
        i=0
        while i<len(nums):
            #get the rest array
            temp=nums[0:i]+nums[i+1:]
            temp_filtered=filter(lambda x: x!=nums[i],temp)
            temp_filtered=list(temp_filtered)
            temp_filtered.sort()
            print(temp_filtered)
            if len(temp_filtered)>=2:
                if temp_filtered[0]<nums[i] and temp_filtered[-1]>nums[i]:
                    count=count+1
            
            
            i=i+1
        return count
        