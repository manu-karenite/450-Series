#https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        ct=0
        sm=0
        lis=list(s)
        for x in lis:
            if x=="L":
                sm-=1
                
                
            else:
                sm+=1
            if sm==0:
                ct+=1
        return(ct)
                
            
            
        