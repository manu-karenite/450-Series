#https://leetcode.com/problems/find-closest-number-to-zero/

from math import fabs
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

    
        d={}
        for x in nums:
            z=int(fabs(x))
            if z in d:
                temp=d[z]
                temp.append(x)
            else:
                d[z]=[x]
        print(d)
        
        value=[]
        mini=2**31
        for x in d:
            if x<mini:
                mini=x
                value=d[x]
        
        print(value)
        value.sort()
        return value[-1]
            

        