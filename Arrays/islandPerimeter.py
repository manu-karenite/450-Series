#https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter=0
        rows=len(grid)
        i=0
        while i<rows:
            #get the first row
            current_row=grid[i]
            
            columns=len(current_row)
            
            j=0
            while j<columns:
                curr_value=current_row[j]
                if grid[i][j]==0:
                    j=j+1
                    continue
                    
                #check top , take help of i
                if i-1<0 or grid[i-1][j]==0:
                    perimeter=perimeter+1
                #check bottom, take help of i
                if i+1>=rows or grid[i+1][j]==0:
                    perimeter=perimeter+1
                #check left , take help of j
                if j-1<0 or grid[i][j-1]==0:
                    perimeter=perimeter+1
                #check right, take help of j
                if j+1>=columns or grid[i][j+1]==0:
                    perimeter=perimeter+1
                j=j+1
            
            i=i+1
        return perimeter
                
                
            