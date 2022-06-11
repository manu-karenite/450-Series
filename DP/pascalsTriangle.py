#https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lis=[[1]]
        
        print(lis)
        for x in range(1,rowIndex+1):
            temp=lis[x-1]
            #we have temp
            temp.insert(0,0)
            temp.append(0)
            l=[]
            for i in range(0,len(temp)-1):
                l.append(temp[i]+temp[i+1])
            lis.append(l)
        print(lis)
        return lis[-1]