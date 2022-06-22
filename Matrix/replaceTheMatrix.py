#https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        s=len(mat[0])*len(mat)
        if s!=r*c:
            return mat
        fin=[]
        ans=[]
        for x in mat:
            ans=ans+x
        #print(ans)
        l=len(ans)
        for i in range(0,l,c):
            fin.append(ans[i:i+c])
        return fin
        
        
        
        