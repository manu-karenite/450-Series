#https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d={}
        for x in deck:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        print(d)
        ct=10**4+1
        for x in d:
            ct=min(d[x],ct)
        print(ct)
        for x in d:
            ct=gcd(ct,d[x])
        print(ct)
        if ct<2:
            return False
        for x in d:
            if d[x]%ct!=0:
                return False
        return True