#https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        
        count=0
        
        while t[k]!=0:
            for i,x in enumerate(t):
                if x==0:
                    pass
                else:
                    t[i]=t[i]-1
                    count=count+1
                    
                    if t[k]==0:
                        return count
            
            
                    
                    
        
        