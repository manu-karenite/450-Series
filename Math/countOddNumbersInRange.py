#https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        n=high-low+1
        if low%2==0 and high%2==0:
            return n//2
            
            
        elif low%2==1 and high%2==0:
            return n//2
            
        elif low%2==1 and high%2==1:
            return (n//2 + 1)
            
        elif low%2==0 and high%2==1:
            return n//2
            
        
