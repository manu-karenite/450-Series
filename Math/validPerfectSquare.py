#https://leetcode.com/problems/valid-perfect-square/

from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        z=int(sqrt(num))
        return z**2==num
        