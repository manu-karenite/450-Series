# https://leetcode.com/problems/goat-latin/


class Solution:
    def toGoatLatin(self, s: str) -> str:

        s = s.split()
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 1
        ans = []
        for x in s:
            first = x[0:1]
            if first in vowels:
                y = x+"ma"
                y = y+"a"*i
                ans.append(y)

            else:
                y = x[1:]+x[0:1]+"ma"
                y = y+"a"*i
                ans.append(y)
            i = i+1
        return(" ".join(ans))
