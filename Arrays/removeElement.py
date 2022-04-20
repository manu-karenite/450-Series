#https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        leng = len(nums)
        while i<leng:
            #we have the list iterator now
            curr=nums[i]
            if curr==val:
                nums.remove(curr)
            else:    
                i=i+1
            leng=len(nums)
        return len(nums)