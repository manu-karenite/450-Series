#https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            
            a=x*-1
            print (a)
            a=str(a)
            a=a[::-1]
            a=-int(a)
        else:
            a=str(x)
            a=a[::-1]
            a=int(a)
        
        if a>=-(2**31) and a<=(2**31-1):
            return a
        else:
            return 0