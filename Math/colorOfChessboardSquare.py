#https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        l,n=coordinates[0],coordinates[1]
        print(l,n)
        
        ascii=ord(l)
        n=int(n)
        
        if ascii%2==0:
            if n%2==1:
                return True
                
            else:
                return False
                
            
        else:
            if n%2==0:
                return True
                
            else:
                return False
                
            