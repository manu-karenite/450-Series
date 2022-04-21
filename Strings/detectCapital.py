#https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        op1=word.capitalize()
        op2=word.lower()
        op3=word.upper()
        
        return (word==op1 or word==op2 or word==op3)
        