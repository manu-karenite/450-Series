#https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i=0
        z=len(s)
        count=0
        while i<=z-3:
            
            st=s[i:i+3]
            if st[0]!=st[1] and st[1]!=st[2] and st[0]!=st[2]:
                count+=1
            print(st)
            i+=1
        return(count)