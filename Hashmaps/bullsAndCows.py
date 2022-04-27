#https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        #get number of bulls first
        g={}
        s={}
        for i in secret:
            if i in s:
                s[i]=s[i]+1
            else:
                s[i]=1
        for i in guess:
            if i in g:
                g[i]=g[i]+1
            else:
                g[i]=1
        print(s)
        print(g)
        
        bulls=0
        i=0
        while i<len(secret):
            print(secret[i],guess[i])
            if secret[i]==guess[i]:
                bulls=bulls+1
                
                value=s[secret[i]]

                if value==1:
                    s.pop(secret[i])
                else:
                    s[secret[i]]=s[secret[i]]-1
                value=g[secret[i]]
                if value==1:
                    g.pop(secret[i])
                else:
                    g[secret[i]]=g[secret[i]]-1
               
                
            else:
                bulls=bulls+0
            i=i+1
        print("bulls,",bulls)
        cows=0
        for x in g:
            if x in s:
                cows=cows+min(s[x],g[x])
                    
        print(cows)
        
        return str(bulls)+"A"+str(cows)+"B"
        
        