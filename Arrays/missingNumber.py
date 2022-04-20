#https://leetcode.com/problems/missing-number/submissions/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        leng=len(nums)
        
        sum=0
        for x in nums:
            sum=sum+x
        return (-sum+((leng*(leng+1))//2))
        