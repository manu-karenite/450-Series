# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s)-1
        s1 = []
        for x in s:
            s1.append(x)
        print(s1)
        s = s1
        while i <= j:
            if s[i].isalpha() == True and s[j].isalpha() == True:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i = i+1
                j = j-1
            elif s[i].isalpha() == False:
                i = i+1
            elif s[j].isalpha() == False:
                j = j-1
            else:
                i = i+1
                j = j-1
        return("".join(s))
