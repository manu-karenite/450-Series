#https://leetcode.com/problems/complex-number-multiplication/


class Solution:
    def extract(self,s:str):

        lis=s.split("+")

        real=int(lis[0])
        #removing i part from it
        imag=lis[1]
        imag=imag[::-1]
        imag=imag[1:]
        imag=imag[::-1]

        i1=-1
        if imag[0]=='-':
            i1=-1*int(imag[1:])
        else:
            i1=int(imag)
            
        return [real,i1]
    
    def construct(self,real,imag)->str:
        
        if real>=0 and imag>=0:
            s=str(real)+"+"+str(imag)+"i"
            
        elif real<0 and imag>=0:
            s="-"+str(real*-1)+"+"+str(imag)+"i"
            
        elif real<0 and imag<0:
            s="-"+str(real*-1)+"+-"+str(imag*-1)+"i"
            
        elif real>=0 and imag<0:
            s=str(real)+"+-"+str(imag*-1)+"i"
        
        
        return s
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        [r1,i1]=self.extract(num1)
        [r2,i2]=self.extract(num2)
        print(r1,i1,r2,i2)
        
        real=r1*r2-i1*i2
        imag=i1*r2+i2*r1
        
        print(real,imag)
        
        s=self.construct(real,imag)
        return s
        
        
