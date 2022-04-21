#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        a=str(x)
        b=(str(x)[::-1])
        print(a,b)
        return a==b
        