#https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        
        ans=[]
        ans.append(num)
        num=str(num)
        x=len(num)
        for i in range(1,x+1,1):
            #iterate for evry time
            z=num
            lis=list(z)
            if lis[i-1]=='6':
                lis[i-1]='9'
                
            else:
                lis[i-1]='6'
            z="".join(lis)
            ans.append(int(z))
            
        return (max(ans))
                
        