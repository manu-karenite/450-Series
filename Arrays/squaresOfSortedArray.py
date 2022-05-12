#https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for x in nums:
            ans.append(int(x**2))
        ans.sort()
        return ans
        