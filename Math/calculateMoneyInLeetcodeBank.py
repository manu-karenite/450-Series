#https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        
        a=1
        s=0
        while n>=7:
            s=s+(((2*a+6)*7)//2)
            n=n-7
            a=a+1
        print(s,n)
        s=s+(((2*a+(n-1))*n)//2)
        return(s)
        
        
            
        