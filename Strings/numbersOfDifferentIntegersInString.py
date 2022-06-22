#https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        i=0
        while i<len(word):
            c=word[i:i+1]
            if c.isalpha()==True:
                word=word[0:i]+"X"+word[i+1:]
            
            i+=1
        word=word.split("X")
        print(word)
        s=set()
        for x in word:
            if x!="":
                l=int(x)
                s.add(l)
        return len(s)
        

        