# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        count = 0
        a = set(brokenLetters)
        print(a)
        text = text.split()
        for x in text:
            found = False
            for y in x:
                if y in a:
                    found = True
                    break

            if found == False:
                count = count+1

        return count
