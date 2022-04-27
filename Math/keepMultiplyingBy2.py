#https://leetcode.com/problems/keep-multiplying-found-values-by-two/
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        ans=original
        
        while True:
            if original in nums:
                original=2*original
                
                
            else:
                break
                
        return original
        