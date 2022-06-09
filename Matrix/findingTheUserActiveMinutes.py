#https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d={}
        for x in logs:
            idty,time=x[0],x[1]
            if idty in d:
                temp=d[idty]
                temp.add(time)
                d[idty]=temp
            else:
                s=set()
                s.add(time)
                d[idty]=s
        print(d)
        
        logs={}
        for x in d:
            l=len(d[x])
            if l in logs:
                logs[l]+=1
            else:
                logs[l]=1
        print(logs)
        ans=[]
        i=0
        while i<k:
            if i+1 in logs:
                ans.append(logs[i+1])
            else:
                ans.append(0)
            i+=1
        return ans