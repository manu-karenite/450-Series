#https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

from math import fabs
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones=[]
        for i,x in enumerate(boxes):
            if x=="1":
                ones.append(i)
        print(ones)
        s=sum(ones)
        z=len(ones)
        lis=[]
        i=0
        for i,x in enumerate(boxes):
            temp=0
            for z in ones:
                temp=int(fabs(z-i))+temp
            print(temp)
            lis.append(temp)
        return lis
                
            
            
        