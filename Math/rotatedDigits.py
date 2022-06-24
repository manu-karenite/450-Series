#https://leetcode.com/problems/rotated-digits/

class Solution:
    def rotatedDigits(self, n: int) -> int:
        d={}
        d[0]="0"
        d[1]="1"
        d[8]="8"
        
        d[2]="5"
        d[5]="2"
        
        d[6]="9"
        d[9]="6"
        
        print(d)
        def solve(num):
            ans=""
            i=0
            while i<len(str(num)):
                curr=int(str(num)[i:i+1])
                if curr not in d:
                    return False
                ans+=d[curr]
                i+=1
            #print(ans,str(num))
            return ans!=str(num)
                
                
            
            
            
        ct=0
        for x in range(1,n+1,1):
            #print(x)
            l=solve(x)
            
            #print(l)
            if l:
                ct+=1
        return ct
            
                
        
            
        