#https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        dicl={}
        
        for x in s:
            if x not in dicl:
                dicl[x]=1
            else:
                dicl[x]=dicl[x]+1
        
        for y in t:
            if y in dicl:
                dicl[y]=dicl[y]-1
                if dicl[y]==0:
                    dicl.pop(y)
            else:
                return y
        