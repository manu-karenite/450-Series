#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        lis=[]
        p=1
        s=0
        for x in n:
            num=ord(x)-48
            p=p*num
            s=s+num
        return p-s
            