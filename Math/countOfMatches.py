#https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        m=0
        while n>1:
            if n%2==0:
                m+=n//2
                n=n//2
                
                
            else:
                m+=n//2
                n=n//2+1
        return m
                
            
        