#https://leetcode.com/problems/find-greatest-common-divisor-of-array/

from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums),min(nums))
    
        
