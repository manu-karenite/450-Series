#https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis=[]
        for x in s:
            if x.isalnum()==True:
                ascii=ord(x)
                if ascii<=90 and ascii>=65:
                    x=x.lower()
                
                lis.append(x)
                
            else:
                continue
                
        print(lis)
        st="".join(lis)
        print(st)
        rev=st[::-1]
        print(rev)
        if st==rev:
            return True
        else:
            return False
        