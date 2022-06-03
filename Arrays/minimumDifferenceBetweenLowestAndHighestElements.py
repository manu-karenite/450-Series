#https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr=nums[k-1]-nums[0]
        i=1
        while i<=len(nums)-k:
            diff=nums[i+k-1]-nums[i]
            curr=min(curr,diff)
            i+=1
        return curr
        