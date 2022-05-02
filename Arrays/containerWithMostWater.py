#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #we have atleats two
        i=0
        j=len(height)-1
        val=0
        while i<=j:
            val=max(val,min(height[i],height[j])*(j-i))
            if height[i]<height[j]:
                i=i+1
            elif height[i]>height[j]:
                j=j-1
            else:
                i=i+1
                j=j-1
        return(val)
        
        