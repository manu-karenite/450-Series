#https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        ans.append(nums[0])
        i=1
        while i<len(nums):
            ans.append(ans[-1]+nums[i])
            i+=1
        return ans