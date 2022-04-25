# https://leetcode.com/problems/backspace-string-compare/

class Solution:

    def create(self, word: str):
        s = ""
        i = 0
        while i < len(word):
            c = word[i:i+1]
            if c == "#":
                # create a backspace
                s = s[::-1]
                s = s[1:]
                s = s[::-1]
                i = i+1

            else:
                s = s+c
                i = i+1
        return s

    def backspaceCompare(self, s: str, t: str) -> bool:
        lhs = self.create(s)
        rhs = self.create(t)

        if lhs == rhs:
            return True
        else:
            return False
