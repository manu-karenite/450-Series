#https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

from math import fabs
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        print(arr2)
        
        ct=0
        for x in arr1:
            ans=True
            for y in arr2:
                if int(fabs(x-y))<=d:
                    ans=False
            
            if ans:
                ct+=1
        return ct
            
        
        