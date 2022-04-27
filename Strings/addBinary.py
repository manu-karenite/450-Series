#https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lef=0
        
        i=0
        a=a[::-1]
        while i<len(a):
            x=int(a[i:i+1])
            lef=lef+(2**i)*x
            i=i+1
        rig=0
        i=0
        b=b[::-1]
        while i<len(b):
            x=int(b[i:i+1])
            rig=rig+(2**i)*x
            i=i+1
        print(lef,rig)
        
        sum=lef+rig
        
        toBin=bin(sum)
        print(toBin[2:])
        return str(toBin[2:])
            
        