#https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

from math import fabs
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count=0
        x=len(nums)
        for i in range(0,x,1):
            for j in range(i+1,x,1):
                if int(fabs(nums[i]-nums[j]))==k:
                    count+=1
        return count
        
        