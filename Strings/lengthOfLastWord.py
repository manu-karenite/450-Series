#https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=s.split() #all whitespaces
        for word in x:
            if word.isalpha()==False:
                x.remove(word)
        last_word=x[len(x)-1]
        print(last_word)
        return len(last_word)
                