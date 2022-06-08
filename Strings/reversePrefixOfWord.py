#https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx=-1
        i=0
        while i<len(word):
            cr=word[i:i+1]
            if cr==ch:
                idx=i
                break
            i+=1
        print(idx)
        
        if idx!=-1:
            lis=word[0:i+1][::-1]+word[i+1:]
            return lis
        return word
        
        
        