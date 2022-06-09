#https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        r=[]
        mid=[]
        for x in nums:
            if x<pivot:
                l.append(x)
            elif x==pivot:
                mid.append(x)
        
            else:
                r.append(x)
        return l+mid+r