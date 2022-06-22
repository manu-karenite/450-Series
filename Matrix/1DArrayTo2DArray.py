#https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l=len(original)
        if m*n!=l:
            return []
        
        
        #nnow >=
        ans=[]
        for i in range(0,l,n):
            curr=original[i:i+n]
            ans.append(curr)
        return(ans)
        