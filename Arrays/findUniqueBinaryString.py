#https://leetcode.com/problems/find-unique-binary-string/


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s=set(nums)
        print(s)
        count=len(nums)
        low=0
        high=2**count-1
        
        for i in range(high,-1,-1):
            b=bin(i)[2:]
            if b not in s:
                if len(b)!=count:
                    #add 0s in front
                    b="0"*(count-len(b))+b
                return b
        
            
        
        
        