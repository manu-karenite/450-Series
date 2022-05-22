#https://leetcode.com/problems/sum-of-digits-in-base-k/

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        s=0
        while n>0:
            rem=n%k
            n=n//k
            s=s+rem
        return s