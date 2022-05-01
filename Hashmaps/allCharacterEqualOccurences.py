#https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/submissions/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for x in s:
            if x in d:
                d[x]=d[x]+1
            else:
                d[x]=1
            
        print(d)
        
        ans=True
        
        #assign the count to first character
        l=s[0:1]
        count=d[l]
        
        for x in d:
            if d[x]!=count:
                return False
        return True
        