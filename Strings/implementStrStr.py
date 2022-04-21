#https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        leng=len(needle)
        if leng==0:
            return 0
        return haystack.find(needle)
        