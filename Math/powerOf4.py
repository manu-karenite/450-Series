#https://leetcode.com/problems/power-of-four/

from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        z=log(n,4)
        print(z)
        z=int(z)
        return 4**z==n
        