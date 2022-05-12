#https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1={}
        d2={}
        for x in nums1:
            if x in d1:
                d1[x]=d1[x]+1
            else:
                d1[x]=1
        for x in nums2:
            if x in d2:
                d2[x]=d2[x]+1
            else:
                d2[x]=1
        print(d1,d2)
        
        ans=[]
        for x in d1:
            if x in d2:
                lis=[x]*min(d1[x],d2[x])
                ans=ans+lis
        return((ans))
        
        