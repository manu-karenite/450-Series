#https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)
        a=s[:l//2]
        b=s[l//2:]
        print(a,b)
        
        vowel={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i=0
        ct1=0
        ct2=0
        while i<l//2:
            if a[i:i+1] in vowel:
                ct1+=1
            if b[i:i+1] in vowel:
                ct2+=1
            i+=1
        return ct1==ct2
            