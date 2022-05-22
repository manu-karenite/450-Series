#https://leetcode.com/problems/simplified-fractions/

import math
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        lis=[]

        for i in range (2,n+1,1):
            
            
            den=i
            for j in range(1,i,1):
                l=math.gcd(den,j)
                
                frac=str(j//l)+"/"+str(den//l)
                print(frac)
                lis.append(frac)
                
        return(list(set(lis)))
            
        
        