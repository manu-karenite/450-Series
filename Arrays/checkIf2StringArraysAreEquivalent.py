#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        a=""
        for x in word1:
            a+=x
        b=""
        for u in word2:
            b+=u
        return a==b
        