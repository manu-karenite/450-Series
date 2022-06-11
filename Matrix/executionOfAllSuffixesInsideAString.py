#https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:

        x=list(s)

        
        lb=0
        rb=n-1
        ub=0
        db=n-1
        
        ans=[]
        i=0
        while i<len(s):
            row=startPos[0]
            col=startPos[1]
            temp=s[i:]
            #print(temp)
            
           
            ct=0
            broke=False
            for z in temp:
                #print(row,col,z)
                mov_row=0
                mov_col=0
                if z=="L":
                    #print("Executed L")
                    mov_col=-1
                    
                    
                    
                elif z=="U":
                    #print("Executed U")
                    mov_row=-1
                    
                elif z=="R":
                    #print("Executed R")
                    mov_col=1
                    
                elif z=="D":
                    #print("Executed D")
                    mov_row=1
                #print(row,col,z,mov_row,mov_col)
                if col+mov_col>=lb and col+mov_col<=rb and row+mov_row>=ub and row+mov_row<=db:
                    ct+=1
                    row+=mov_row
                    col+=mov_col
                else:
                    ans.append(ct)
                    broke=True
                    break
            if not broke:
                ans.append(ct)
            i+=1
        return(ans)
        
        