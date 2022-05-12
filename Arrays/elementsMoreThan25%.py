#https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        limit=len(arr)//4
        
        for x in arr:
            ct=arr.count(x)
            if ct>limit:
                return x
        
        
        