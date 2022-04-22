#https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        print(len(codes))
        codesdic={}
        i=97
        while i<=122:
            codesdic[chr(i)]=codes[i-97]
            i=i+1
        set_words=set()
        
        for x in words:
            #x is the current word
            ans=""
            for letter in x:
                ans=ans+codesdic[letter]
            
            set_words.add(ans)
        
        return len(set_words)
        