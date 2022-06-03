#https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        columns=len(matrix[0])
        rows=len(matrix)
        i=0
        while i<columns:
            j=0
            temp=[]
            while j<rows:
                temp.append(matrix[j][i])
                j+=1
            ans.append(temp)
            i+=1
        return(ans)
        