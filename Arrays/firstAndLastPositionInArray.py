#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lis=[-1,-1]
        if target in nums:
            idx=nums.count(target)
            print(idx)
            idxx=nums.index(target)
            lis[0]=idxx
            lis[1]=idxx+idx-1
            
        
        return lis
        