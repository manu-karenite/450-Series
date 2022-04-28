#https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i,item in enumerate(nums):
            ans.append(nums[nums[i]])
        print(ans)
        return ans
        