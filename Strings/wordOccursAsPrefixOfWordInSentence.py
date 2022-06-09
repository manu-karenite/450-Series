#https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        i=0
        s=sentence.split(" ")
        while i<len(s):
            curr=s[i]
            if searchWord in curr:
                idx=curr.index(searchWord)
                if idx==0:
                    return i+1
            i+=1
        return -1
        