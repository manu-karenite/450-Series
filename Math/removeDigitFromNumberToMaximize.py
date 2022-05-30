#https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        a=set()
        i=0
        z=len(number)
        while i<z:
            
            cr=number[i:i+1]
            print(cr)
            if cr==digit:
                dupli=number
                dupli=dupli[0:i]+dupli[i+1:]
                print(dupli)
                a.add(dupli)
            i=i+1
        print(a)
        z=list(a)
        return max(z)