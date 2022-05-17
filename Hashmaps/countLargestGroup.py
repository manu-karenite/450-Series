#https://leetcode.com/problems/count-largest-group/
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        for x in range(1,n+1,1):
            sum=0
            temp=x
            while temp!=0:
                sum=sum+temp%10
                temp=temp//10
            #print(sum)
            if sum in d:
                d[sum]=d[sum]+1
            else:
                d[sum]=1
            
        print(d)
        lis=[]
        for x in d:
            lis.append(d[x])
        print(lis)
        lis.sort()
        
        m=lis[-1]
        return lis.count(m)
