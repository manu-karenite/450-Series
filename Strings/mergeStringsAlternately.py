#https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        p=len(word1)
        q=len(word2)
        s=""
        while i<p and j<q:
            a=word1[i:i+1]
            b=word2[j:j+1]
            s=s+a+b
            i+=1
            j+=1
        
        print(s)
        if i<p:
            s=s+word1[i:]
        
        if j<q:
            s=s+word2[j:]
        
        return s
            
        