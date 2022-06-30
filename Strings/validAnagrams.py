#https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for x in s:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        print(d)
        
        for x in t:
            if x not in d:
                return False
            d[x]-=1
            if d[x]==0:
                d.pop(x)
                
        return len(d)==0
    