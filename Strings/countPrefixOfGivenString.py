#https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ct=0
        for x in words:

            if x in s:
                idx=s.index(x)
                if idx==0:
                    ct+=1
        return ct
        