#https://leetcode.com/problems/second-largest-digit-in-a-string/

class Solution:
    def secondHighest(self, s: str) -> int:
        a=set()
        for x in s:
            if ord(x)>=48 and ord(x)<=57:
                a.add(int(x))
        print(a)
        if len(a)<=1:
            return -1
        else:
            x=list(a)
            x.sort()
            return x[-2]
                               
        