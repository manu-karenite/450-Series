#https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans=[]
        for i,item in enumerate(nums):
            ans.insert(index[i],item)
        return ans
        