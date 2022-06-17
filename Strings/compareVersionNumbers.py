#https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a=version1.split(".")
        b=version2.split(".")
        
        a=[int(x) for x in a]
        b=[int(y) for y in b]
        
        al=len(a)
        bl=len(b)
        if al<bl:
            a=a+[0]*(bl-al)
        elif bl<al:
            b=b+[0]*(al-bl)
        al=len(a)
        bl=len(b)
        
        print(a,b)
        i=0
        j=0
        while i<al and j<bl:
            #common tak chalna hai
            print(a[i],b[j])
            if a[i]<b[j]:
                return -1
            if a[i]>b[j]:
                return 1
            i+=1
            j+=1
        return 0
        