#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        vount=0
        for x in nums:
            x=str(x)
            x=list(x)
            
            if len(x)%2==0:
                vount=vount+1
        return vount
        