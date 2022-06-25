#https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        ans=[]
        for x in matrix:
            ans+=x
        ans.sort()
        return ans[k-1]
        