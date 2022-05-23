#https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        columns=len(mat[0])
        #these are the m * n format
        
        #handle rows first
        for i in range(0,columns,1):
            r=0
            s=i
            lis=[]
            while r<rows and s<columns:
                lis.append(mat[r][s])
                r+=1
                s+=1
            #now lis is formed
            lis.sort()
            
            r=0
            s=i
            k=0
            while r<rows and s<columns:
                mat[r][s]=lis[k]
                r+=1
                k+=1
                s+=1
        print(mat)
        
        for i in range(0,rows,1):
            r=i
            s=0
            lis=[]
            while r<rows and s<columns:
                lis.append(mat[r][s])
                r+=1
                s+=1
            #now lis is formed
            lis.sort()
            
            r=i
            s=0
            k=0
            while r<rows and s<columns:
                mat[r][s]=lis[k]
                r+=1
                k+=1
                s+=1
        print(mat)
        return mat
        
        
                
            
            
        