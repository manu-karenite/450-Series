#https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ct=0
        for x in words:
            if pref in x:
                idx=x.index(pref)
                if idx==0:
                    ct+=1
        return ct
        