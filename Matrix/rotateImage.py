#https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        columns=len(matrix[0])
        ans=[]
        for i in range(0,rows):
            temp=[-1]*columns
            ans.append(temp)

        
        sc=0
        while sc<rows:
            j=0
            while j<columns:
                ans[j][columns-1-sc]=matrix[sc][j]
                j+=1
            sc+=1

        
        i=0
        while i<rows:
            j=0
            while j<columns:
                matrix[i][j]=ans[i][j]
                j+=1
            i+=1

        