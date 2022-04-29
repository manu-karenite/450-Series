#https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def getAns(self,word):
        i=0
        j=len(word)-1
        while i<=j:
            if word[i:i+1]!=word[j:j+1]:
                return False
            i=i+1
            j=j-1
        return True
                
    def firstPalindrome(self, words: List[str]) -> str:
        ans=""
        for x in words:
            ans=self.getAns(x)
            if ans==True:
                return x
            
        return ""
        