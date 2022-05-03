#https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
    
        #no 0s are there
        count=0
        for x in nums:
            if x<0:
                count=count+1
        
        if count%2==0:
            return 1
        else:
            return -1
        