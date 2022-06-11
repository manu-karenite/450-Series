#https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        f={}
        for x in s:
            if x in f:
                f[x]+=1
            else:
                f[x]=1
        print(f)
        s=""
        for z in order:
            if z in f:
                temp=[z]*f[z]
                temp="".join(temp)
                s=s+temp
                f.pop(z)
        print(s,f)
        rem=""
        for x in f:
            t=[x]*f[x]
            t="".join(t)
            s=s+t
        return s
            
            
                
            
        