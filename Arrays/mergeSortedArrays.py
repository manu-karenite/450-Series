#https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        j=0
        ans=[]
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                ans.append(nums1[i])
                i=i+1
            else:
                ans.append(nums2[j])
                j=j+1
        
        if i!=m: #means something is left
            temp=nums1[i:m]
            for x in temp:
                ans.append(x)
            
        if j!=n:
            temp=nums2[j:]
            for y in temp:
                ans.append(y)
        
        print(ans)
        nums1.clear()
        for h in ans:
            nums1.append(h)
        
        
        