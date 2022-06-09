#https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i=0
        j=len(piles)-1
        
        s=0
        while i<j-1: # 3 consecutive
            s+=piles[j-1]
            i+=1
            j-=2
        return s
            
        
        