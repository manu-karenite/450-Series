#https://leetcode.com/problems/power-of-two/

from math import log
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        
        #only for positive now
        x=log(n,2)
        if 2**int(x)!=n:
            return False
        else:
            return True
        
        