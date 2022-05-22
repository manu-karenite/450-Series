#https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        lis=s.split(" ")
        rem=[]
        for x in lis:
            if x.isnumeric()==True:
                rem.append(int(x))
        print(rem)
        
        i=1
        z=len(rem)
        while i<z:
            if rem[i]<=rem[i-1]:
                return False
            i=i+1
        return True