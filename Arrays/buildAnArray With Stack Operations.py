#https://leetcode.com/problems/build-an-array-with-stack-operations/


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        lis=[]
        for x in range(1,n+1,1):
            lis.append(x)
        i=0 #for target array
        j=0 #for lis
        t=[]
        print(lis,target)
        while i<len(target):
            if lis[j]==target[i]:
                t.append("Push")
                i+=1
                j+=1
            else:
                t.append("Push")
                t.append("Pop")
                j+=1
        return(t)
        
            
            
            