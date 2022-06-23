#https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

from math import log
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n<=1:
            return True
        
        ans=int(log(n,3))
        print(ans)
        while ans>=0:
            x=3**ans
            if x<=n:
                n-=x
            else:
                pass
            if n==0:
                return True
            ans-=1
        
        return False
        
        