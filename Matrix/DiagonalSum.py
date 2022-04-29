#https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        leng=len(mat)
        sum=0
        for i in range(0,leng):
            sum=sum+mat[i][i] #pd
            sum=sum+mat[i][leng-1-i]
        
        if leng%2==1:
            #odd
            sum=sum-mat[int(leng/2)][int(leng/2)]
        return sum
            
            
            
        