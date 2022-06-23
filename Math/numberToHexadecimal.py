#https://leetcode.com/problems/convert-a-number-to-hexadecimal/


class Solution:
    
    def pos(self,num,d):
        print(d)
        ans=""
        while num>0:
            rem=num%16
            ans+=d[rem]
            num=num//16
        return ans[::-1]
            
        
    def toHex(self, num: int) -> str:
        d={}
        for i in range(0,10):
            d[i]=str(i)
            
        d[10]="a"
        d[11]="b"
        d[12]="c"
        d[13]="d"
        d[14]="e"
        d[15]="f"
        if num==0:
            return "0"
        if num>0:
            return self.pos(num,d)
        else:
            num += 2 ** 32
            return self.pos(num,d)
        