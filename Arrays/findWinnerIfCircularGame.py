#https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lis=[]
        for i in range(1,n+1,1):
            lis.append(i)
        #print(lis)
        
        start=0
        while len(lis)>1:
            #print(lis)
            last=(start+k-1)%len(lis)
            lis=lis[0:last]+lis[last+1:]
            if last==len(lis)-1:
                start=last
                
            else:
                
                start=last
        
        return(lis[0])
                
                
            